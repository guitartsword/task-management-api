from sqlmodel import SQLModel, Session, create_engine

from .security import get_password_hash
from .config import DATABASE_URL


engine = create_engine(DATABASE_URL)


def drop_db():
    from models import tasks, users
    SQLModel.metadata.drop_all(engine)


def init_db():
    from models import tasks, users
    SQLModel.metadata.create_all(engine)


def seed_db():
    import random
    from models import tasks, users
    with Session(engine) as session:
        password = get_password_hash("test1234")
        user1 = users.User(
            email="user1@test.com",
            hashed_password=password
        )
        user2 = users.User(
            email="user2@test.com",
            hashed_password=password
        )
        session.add_all([user1, user2])
        session.commit()
        session.refresh(user1)
        session.refresh(user2)
        tasks_to_add = [
            tasks.Task(
                title=f'task {idx+1}',
                description=f'[{idx+1}]Natus quas consequatur consectetur vel totam cupiditate est a.',
                status=random.choice(['todo', 'doing', 'done']),
                owner_id=random.choice([user1.id, user2.id]),
            ) for idx in range(50)
        ]
        session.add_all(tasks_to_add)
        session.commit()
