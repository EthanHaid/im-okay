from fastapi import APIRouter
from ..helpers import twilio_client

router = APIRouter(prefix="/message")


@router.get("/send")
def send_disaster_message(phone_number: str):
    message = twilio_client.send_disaster_message(phone_number, "FAKE DISASTER")
    return 200
