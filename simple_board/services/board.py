from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select
from repository.models.board import Board
from repository.models.comment import Comment
from schemas.board import BoardCreate, BoardUpdate
from exceptions.board import BoardNotFoundException, BoardForbiddenException
from exceptions.user import UserCredentialsException
from repository.models.user import User
import math


def create(db: Session, data: BoardCreate, currnet_user: User):

    board = Board(
        title=data.title, contents=data.contents, user_id=currnet_user.user_id
    )
    db.add(board)
    db.commit()
    db.refresh(board)
    return board


def update(db: Session, data: BoardUpdate, id: int, current_user: User):
    board = db.get(Board, id)

    if board is None:
        raise BoardNotFoundException

    if board.user_id != current_user.user_id:
        raise UserCredentialsException

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


# 전체 조회 + 검색
def select_all(db: Session, page: int, size: int, criteria: str, keyword: str):
    query = db.query(Board)

    if keyword:
        if criteria == "tc":
            query = query.filter(
                Board.title.contains(keyword) | Board.title.contains(keyword)
            )
        elif criteria == "t":
            query = query.filter(Board.title.contains(keyword))
        elif criteria == "w":
            query = query.join(Board.user).filter(User.name.contains(keyword))

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
        "criteria": criteria,
        "keyword": keyword,
    }


def select_recents(db: Session):
    query = db.query(Board)
    boards = query.order_by(Board.created_at.desc()).limit(4).all()
    return boards


def delete(db: Session, id: int, current_user: User):

    board = db.get(Board, id)

    if board is None:
        raise BoardNotFoundException
    if board.user_id != current_user.user_id:
        raise UserCredentialsException
    db.delete(board)
    db.commit()
    return id
