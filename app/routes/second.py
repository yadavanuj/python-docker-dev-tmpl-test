from fastapi import APIRouter

router = APIRouter()

@router.get("/second")
def from_second_route():
    return "Hello from second route"