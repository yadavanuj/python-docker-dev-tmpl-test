from typing import Optional

from sqlmodel import Field, SQLModel
from app.config import settings


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post: str
