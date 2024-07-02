from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from api.deps import SessionDep
from models.tasks import MessageResponse, Task, TaskCreate, TaskListResponse

router = APIRouter()


@router.get("/", response_model=TaskListResponse)
def read_tasks(session: SessionDep, skip: int = 0, limit: int = 10):
    statement = (
        select(Task)
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
def get_task_detail(session: SessionDep, id: int):
    return session.get(Task, id)


@router.post("/", response_model=Task)
def create_task(session: SessionDep, item_in: TaskCreate):
    task = Task.model_validate(item_in)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.put("/{id}", response_model=Task)
def update_task(session: SessionDep, id:int, item_in: TaskCreate):
    item = session.get(Task, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    update_dict = item_in.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_dict)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{id}", response_model=MessageResponse)
def delete_task(session: SessionDep, id:int):
    item = session.get(Task, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return MessageResponse(message="Task deleted successfully")
