from fastapi import APIRouter

from ..helpers.FirebaseClient import FirebaseClient
from ..models import DisasterInput, DisasterFireBase
from ..models import DisasterResponseInput, DisasterResponseFireBase
from typing import List

PREFIX = 'disasters'
router = APIRouter(prefix='/' + PREFIX)


@router.get("/")
def get_disasters() -> List[DisasterResponseFireBase]:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    data = db.child(PREFIX).get()
    return list(data)


@router.get("/{disaster_id}")
def get_disaster(disaster_id: str) -> DisasterResponseFireBase:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster = db.child(PREFIX).child(disaster_id).get()
    return disaster


@router.post("/")
def create_disaster(disaster: DisasterInput) -> DisasterFireBase:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster = db.child(PREFIX).push(disaster.dict())
    return disaster


@router.post("/response")
def create_disaster_response(disaster_response: DisasterResponseInput) -> DisasterResponseFireBase:

    return 200
