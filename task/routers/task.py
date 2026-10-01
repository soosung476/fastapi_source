from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from schemas.model import TaskCreate, TaskResponse, TaskPageResponse, TaskUpdate
from repository.database import get_db
from fastapi import Depends
from services.task import create, select, update, delete
from exceptions.task import TaskNotFoundException

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])


# Depends : 주입
@task_router.post("", response_model=dict)
async def post_tasks(data: TaskCreate, db: Session = Depends(get_db)) -> dict:

    task = create(data, db=db)

    return {"message": f"Task {task.id} 삽입 성공"}


@task_router.get("", response_model=TaskPageResponse)
async def get_tasks(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    tasks = select(page=page, size=size, db=db)
    return tasks


@task_router.put("/{id}", response_model=dict)
async def put_task(id: int, update_task: TaskUpdate, db: Session = Depends(get_db)):
    try:
        task = update(db=db, data=update_task, id=id)

    except TaskNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="해당하는 task가 없습니다"
        )

    return {"message": f"Task {task.id}수정 완료"}


@task_router.delete("/{id}", response_model=dict)
async def delete_task(id: int, db: Session = Depends(get_db)):
    try:
        id = delete(id=id, db=db)
    except TaskNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"message": f"Task {id}삭제 완료"}
