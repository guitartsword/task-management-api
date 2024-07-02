from sqlmodel import SQLModel, create_engine

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def init_db():
    from models import tasks
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()