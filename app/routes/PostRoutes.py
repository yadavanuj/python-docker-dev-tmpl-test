import logging
from typing import Any
from fastapi import APIRouter, Body, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.services.PostService import create_post_service
from app.models import Post
from sqlmodel import Session

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

# declare post service
post_service = None


def bind(engine: Any):
    # bind the engine to the session
    session = Session(bind=engine)
    # initialize post service
    global post_service
    post_service = create_post_service(session)

@router.post("/posts/")
async def create_post(post: Post.Post):
    logger.info(post)
    new_post = post_service.create_post(post.post)
    return JSONResponse(content={"id": new_post.id, "post": new_post.post}, status_code=201)

@router.get("/posts/")
async def read_posts():
    posts = post_service.get_all_posts()
    return JSONResponse(content=[{"id": post.id, "post": post.post} for post in posts], status_code=200)

@router.get("/posts/{id}")
async def read_post(id: int):
    post = post_service.get_post_by_id(id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return JSONResponse(content={"id": post.id, "post": post.post}, status_code=200)

@router.patch("/posts/{id}")
async def update_post(id: int, post: str):
    updated_post = post_service.update_post(id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return JSONResponse(content={"id": updated_post.id, "post": updated_post.post}, status_code=200)

@router.delete("/posts/{id}")
async def delete_post(id: int):
    if not post_service.delete_post(id):
        raise HTTPException(status_code=404, detail="Post not found")
    return Response(status_code=204)
