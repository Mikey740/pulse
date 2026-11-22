
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to Pulse",
        "status": "operational"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
