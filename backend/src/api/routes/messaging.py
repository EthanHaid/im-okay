from fastapi import APIRouter
from ..helpers import TwilioClient
from fastapi import File, UploadFile
from typing import List
from ..config import *
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter(prefix="/message")


@router.post("/send/csv")
async def send_disaster_message_csv(disaster_id: str, file: UploadFile = File(...)):
    # Parse list of numbers from CSV
    file_contents = await file.read()
    parsed_numbers = file_contents.split(',')
    # TODO: Validation for actual numbers but who has the time for that, right?

    # Send message to all
    return _send_disaster_message_to_numbers(disaster_id, parsed_numbers)


@router.post("/send/list")
async def send_disaster_message_list(disaster_id: str, phone_numbers: List[str]):
    return _send_disaster_message_to_numbers(disaster_id, phone_numbers)


@router.post("/send")
def send_disaster_message(phone_number: str, disaster_id: str) -> str:
    return _send_disaster_message_to_numbers(disaster_id, [phone_number])[0]


@router.post("/custom")
def send_custom_message(phone_number: str, message: str) -> str:
    twilio_client = TwilioClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER)
    message = twilio_client.send_message(phone_number, message)
    return message.sid


@router.post("/reply")
def send_message_reply() -> str:
    """
    Responds to incoming messages
    This route will be directly called by Twilio on the production server
    """
    resp = MessagingResponse()
    message = resp.message("Hi again! Please use the previously sent URL to proceed 🙏")
    return message.sid


def _send_disaster_message_to_numbers(disaster_id: str, numbers: List[str]) -> List[str]:
    twilio_client = TwilioClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER)
    messages = twilio_client.send_bulk_disaster_messages(numbers, disaster_id)
    return [message.sid for message in messages]

