from datetime import datetime, timedelta
import enum
from typing import Optional

from sqlmodel import Field, SQLModel

class StatusOptions(enum.Enum):
    todo = 'todo'
    doing = 'doing'
    done = 'done'

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=128)
    description: str = Field()
    status: StatusOptions = Field(default=StatusOptions.todo)
    due_date: datetime = Field(default=datetime.now()+timedelta(days=1))

class TaskListResponse(SQLModel):
    data: list[Task]
    count: int

class TaskCreate(SQLModel):
    title: str = Field(min_length=1, max_length=128)
    description: str = Field()
    status: Optional[StatusOptions] = Field(default=StatusOptions.todo)
    due_date: Optional[datetime] = Field(default=datetime.now()+timedelta(days=1))

class MessageResponse(SQLModel):
    message: str