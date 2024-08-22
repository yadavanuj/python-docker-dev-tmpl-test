from fastapi import APIRouter
from app.services.SimplePandasService import serve

router = APIRouter()

@router.get("/simple-pandas")
def simple_pandas_route():
    return serve()