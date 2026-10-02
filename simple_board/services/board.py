from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from repository.models.board import Board
from repository.models.comment import Comment
from schemas.board import BoardCreate, BoardUpdate
from exceptions.board import BoardNotFoundException
import math


def create(db: Session, data: BoardCreate):

    board = Board(title=data.title, contents=data.contents, user_id=data.user_id)
    db.add(board)
    db.commit()
    db.refresh(board)
    return board


def update(db: Session, data: BoardUpdate, id: int):
    board = db.get(Board, id)

    if board is None:
        raise BoardNotFoundException

    if data.title is not None:
        board.title = data.title
    if data.contents is not None:
        board.contents = data.contents

    db.commit()
    return id


# def select_one(db: Session, id: int):
#     board = db.get(Board, id)
#     if board is None:
#         raise BoardNotFoundException
#     return board


def select_one(db: Session, id: int):
    stmt = (
        select(Board)
        .options(
            selectinload(Board.user),
            selectinload(Board.comments).selectinload(Comment.user),
        )
        .where(Board.id == id)
    )
    board = db.scalar(stmt)

    if board is None:
        raise BoardNotFoundException
    return board


def select_all(db: Session, page: int, size: int):
    query = db.query(Board)

    total = query.count()
    offset = (page - 1) * size
    boards = query.order_by(Board.id.desc()).offset(offset).limit(size).all()
    total_pages = math.ceil(total / size)

    return {
        "items": boards,
        "total": total,
        "page": page,
        "size": size,
        "total_pages": total_pages,
    }


def select_recents(db: Session):
    query = db.query(Board)
    boards = query.order_by(Board.created_at.desc()).limit(4).all()
    return boards


def delete(db: Session, id: int):

    board = db.get(Board, id)

    if board is None:
        raise BoardNotFoundException
    db.delete(board)
    db.commit()
    return id
