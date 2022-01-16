from fastapi import APIRouter

from ..helpers.FirebaseClient import FirebaseClient
from ..models import DisasterInput, DisasterCreate, DisasterFireBase, DisasterResponseCreate
from ..models import DisasterResponseInput, DisasterResponseFireBase
from typing import List
import datetime

PREFIX = 'disasters'
router = APIRouter(prefix='/' + PREFIX)


@router.get("/")
def get_disasters() -> List[DisasterFireBase]:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disasters = db.child(PREFIX).get().each()

    result = []
    for disaster in disasters:
        # Parse responses because its wack. Same format as the comment below
        if 'responses' in disaster.item[1].keys():
            responses = disaster.item[1]['responses']
            responses = [DisasterResponseFireBase(id=key, **responses[key]) for key in responses.keys()]
            disaster.item[1]['responses'] = responses

        # Iterate through each item in the list and format properly
        # Pyrebase returns in a wack { item : [id, object_values] } format so deal with that crap
        result.append(DisasterFireBase(
            id=disaster.item[0],
            **disaster.item[1],
        ))
        print(disaster.item[0])

    return result


@router.get("/{disaster_id}")
def get_disaster(disaster_id: str) -> DisasterFireBase:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster = db.child(PREFIX).child(disaster_id).get()
    return disaster


@router.post("/")
def create_disaster(disaster_input: DisasterInput) -> DisasterFireBase:
    disaster = DisasterCreate(**disaster_input.dict(), timestamp=datetime.datetime.now().__str__())

    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster = db.child(PREFIX).push(disaster.dict())
    return disaster


@router.put("/response/{disaster_id}/{disaster_response_id}")
def update_disaster_response(disaster_id: str, disaster_response_id: str,
                             disaster_response_input: DisasterResponseInput) -> DisasterFireBase:
    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster_response_record = db.child(PREFIX).child(disaster_id).child('responses').child(disaster_response_id)

    # Update fields
    disaster = disaster_response_record.update({
        'is_ok': disaster_response_input.is_ok,
        'message': disaster_response_input.message,
        'location:': disaster_response_input.location.dict()
    })

    return disaster


@router.post("/response/{disaster_id}")
def create_disaster_response(disaster_id: str, disaster_response_input: DisasterResponseInput) -> DisasterFireBase:
    return handle_create_disaster_response(disaster_id, disaster_response_input)


def handle_create_disaster_response(disaster_id: str, disaster_response_input: DisasterResponseInput):
    # Add timestamp
    disaster_response = DisasterResponseCreate(**disaster_response_input.dict(),
                                               timestamp=datetime.datetime.now().__str__())

    firebase_client = FirebaseClient()
    db = firebase_client.get_db()
    disaster = db.child(PREFIX).child(disaster_id).child('responses').push(disaster_response.dict())
    return disaster
