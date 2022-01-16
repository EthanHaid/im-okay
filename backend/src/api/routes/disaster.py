from fastapi import APIRouter
from ..models import DisasterInput, DisasterFireBase
from ..models import DisasterResponseInput, DisasterResponseFireBase
router = APIRouter(prefix="/disaster")


@router.get("/{disaster_id}")
def get_disaster(disaster_id: str) -> DisasterResponseFireBase:
    return 200

@router.post("/")
def create_disaster(disaster: DisasterInput) -> DisasterFireBase:
    return 200

@router.post("/response")
def create_disaster_response(disaster_response: DisasterResponseInput) -> DisasterResponseFireBase:
    return 200