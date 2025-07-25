from dotenv import load_dotenv
import os
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from app.config import settings
from app.routes import PostRoutes, CuriousRoutes, SimpleRoutes, SimplePandasRoutes

load_dotenv()  # take environment variables from .env.

# Fetch environment variables
hostName = str(settings.HOST_NAME)
serverPort = int(settings.SERVER_PORT)

sql_engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables():
    """
    Create the database and tables using SQLModel metadata

    This function is called on startup to ensure the database is created
    and tables are defined.
    """
    SQLModel.metadata.create_all(sql_engine)


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


PostRoutes.bind(sql_engine)
app.include_router(PostRoutes.router, prefix="/api/v1", tags=["posts"])
app.include_router(SimpleRoutes.router, prefix="/api/v1", tags=["second"])
app.include_router(CuriousRoutes.router, prefix="/api/v1", tags=["asks"])
app.include_router(SimplePandasRoutes.router, prefix="/api/v1", tags=["pandas"])
