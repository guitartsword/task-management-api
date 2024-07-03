from datetime import datetime, timedelta
import enum
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from models.users import User

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
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User = Relationship(back_populates="tasks")

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