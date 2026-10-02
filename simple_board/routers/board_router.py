from fastapi import APIRouter, HTTPException, status
from schemas.board import BoardUpdate, BoardCreate, BoardResponse, BoardPageResponse
from services.board import (
    create,
    update,
    delete,
    select_all,
    select_one,
    select_recents,
)
from sqlalchemy.orm import Session
from fastapi import Depends
from repository.database import get_db
from exceptions.board import BoardNotFoundException

board_router = APIRouter(tags=["Boards"])

# 전체 조회 + GET: http://localhost:8000/boards
# 하나 조회 + GET: http://localhost:8000/boards/1
# 하나 수정 + PUT: http://localhost:8000/boards/1 + 수정데이터
# 하나 삭제 + DELETE: http://localhost:8000/boards/1
# 댓글 조회 + http://localhost:8000/boards/1/comments


@board_router.get("", response_model=BoardPageResponse)
async def get_boards(db: Session = Depends(get_db), page: int = 1, size: int = 10):
    result = select_all(db=db, page=page, size=size)
    return result


@board_router.post("", response_model=dict)
async def post_board(data: BoardCreate, db: Session = Depends(get_db)):
    try:
        board = create(db=db, data=data)

    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="서버 오류가 발생했습니다 잠시 후에 시도해주세요.",
        )
    return {"message": f"{board.id}번이 삽입되었습니다."}


@board_router.get("/recents", response_model=list[BoardResponse])
async def get_recents(db: Session = Depends(get_db)):
    result = select_recents(db=db)
    return result


@board_router.get("/{id}", response_model=BoardResponse)
async def get_board(id: int, db: Session = Depends(get_db)):
    try:
        board = select_one(db=db, id=id)
    except BoardNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 board를 찾을 수 없습니다.",
        )
    return board


@board_router.put("/{id}", response_model=dict)
async def put_board(
    id: int, update_board: BoardUpdate, db: Session = Depends(get_db)
) -> dict:
    try:
        id = update(id=id, db=db, data=update_board)

    except BoardNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 board를 찾을 수 없습니다.",
        )
    return {"message": f"{id}번이 수정되었습니다"}


@board_router.delete("/{id}", response_model=dict)
async def delete_board(id: int, db: Session = Depends(get_db)):
    try:
        id = delete(db=db, id=id)

    except BoardNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 board를 찾을 수 없습니다.",
        )
    return {"message": f"{id}번이 삭제되었습니다"}


# @board_router.get("/{id}/comments", response_model=list[Comment])
# async def get_board_comments(id: int):
#     return []
