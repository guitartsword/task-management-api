from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from api.deps import CurrentUser, SessionDep
from models.tasks import MessageResponse, Task, TaskCreate, TaskListResponse

router = APIRouter()


@router.get("/", response_model=TaskListResponse)
def read_tasks(session: SessionDep, user: CurrentUser, skip: int = 0, limit: int = 10):
    statement = (
        select(Task)
        .where(Task.owner_id == user.id)
        .offset(skip)
        .limit(limit)
    )
    count_satetement = (
        select(func.count())
        .select_from(Task)
    )
    count = session.exec(count_satetement).one()
    tasks = session.exec(statement).all()
    return TaskListResponse(data=tasks, count=count)

@router.get("/{id}", response_model=Task)
def get_task_detail(session: SessionDep, user: CurrentUser, id: int):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Item not found")
    if task.owner_id != user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return task


@router.post("/", response_model=Task)
def create_task(session: SessionDep, user: CurrentUser, item_in: TaskCreate):
    task = Task.model_validate(item_in, update={ "owner_id": user.id })
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.put("/{id}", response_model=Task)
def update_task(session: SessionDep, user: CurrentUser, id:int, item_in: TaskCreate):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Item not found")
    if task.owner_id != user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = item_in.model_dump(exclude_unset=True)
    task.sqlmodel_update(update_dict)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{id}", response_model=MessageResponse)
def delete_task(session: SessionDep, user: CurrentUser, id:int):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Item not found")
    if task.owner_id != user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(task)
    session.commit()
    return MessageResponse(message="Task deleted successfully")
