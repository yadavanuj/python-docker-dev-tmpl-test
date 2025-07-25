import logging
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.services import CuriousService
from app.models import Post
from app.services.pii_detection_service import PIIDetectionService
from app.models import PIIDetectionResponse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

pii_detector = PIIDetectionService()


@router.post("/ask/")
async def ask(post: Post.Post):
    logger.info("Ask was: ")
    logger.info(post.post)
    response = await CuriousService.ask(post.post)
    return JSONResponse(content=response, status_code=201)

@router.post("/detect-pii/", response_model=PIIDetectionResponse)
async def detect_pii(text: str = Body(..., embed=True)):
    logger.info(f"Detecting PII in text: {text}")
    detections = pii_detector.detect_pii(text)
    return {"detections": detections}
