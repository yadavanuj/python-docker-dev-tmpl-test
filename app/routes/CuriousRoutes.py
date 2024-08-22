import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services import CuriousService
from app.models import Post

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/ask/")
async def ask(post: Post.Post):
    logger.info("Ask was: ")
    logger.info(post.post)
    response = await CuriousService.ask(post.post)
    return JSONResponse(content=response, status_code=201)