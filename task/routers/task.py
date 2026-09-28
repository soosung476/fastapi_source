from fastapi import APIRouter, HTTPException, status
from models.model import Task

task_router = APIRouter(prefix="/tasks")

datas = [
    {"id": 0, "text": "Visit kafka Museum", "done": True},
    {"id": 1, "text": "Watch a puppet show", "done": False},
    {"id": 2, "text": "Lennon wall pic", "done": False},
]

tasks = [Task(**task) for task in datas]


@task_router.get("", response_model=list[Task])
async def get_tasks():
    return tasks


@task_router.post("", response_model=Task)
async def post_task(text: str):
    new_id = max((task.id for task in tasks), default=-1) + 1
    data = Task(id=new_id, text=text, done=False)
    tasks.append(data)
    return data


@task_router.put("", response_model=Task)
async def put_task(update_task: Task):
    for task in tasks:
        if task.id == update_task.id:
            task.text = update_task.text
            task.done = update_task.done
            return task
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@task_router.delete("", response_model=list[Task])
async def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return tasks
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
