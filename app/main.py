from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.config import settings
from app.routes import PostRouter, second

hostName = "localhost"
serverPort = 8000

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables():
    """
    Create the database and tables using SQLModel metadata

    This function is called on startup to ensure the database is created
    and tables are defined.
    """
    SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.on_event("startup")
def on_startup():
    """
    Startup event handler

    Called when the application starts. Creates the database and tables.
    """
    create_db_and_tables()
    print(f"Server started on {hostName}:{serverPort}")

@app.get("/")
def read_root():
    return {"message": "Hello World!"}


PostRouter.bind(engine)
app.include_router(PostRouter.router, prefix="/api/v1", tags=["posts"])
app.include_router(second.router, prefix="/api/v1", tags=["second"])

    