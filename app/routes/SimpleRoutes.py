from fastapi import APIRouter

router = APIRouter()


@router.get("/sample")
def from_sample_route():
    return "Hello from sample route"
