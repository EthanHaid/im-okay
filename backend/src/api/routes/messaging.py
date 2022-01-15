from fastapi import APIRouter
from ..helpers import TwilioClient
from fastapi import File, UploadFile
from typing import List
from ..config import *
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter(prefix="/message")


@router.post("/send/csv")
async def send_disaster_message_csv(disaster_id: str, file: UploadFile = File(...)):
    twilio_client = TwilioClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER)

    # Parse list of numbers from CSV
    file_contents = await file.read()
    parsed_numbers = file_contents.split(',')
    # TODO: Validation for actual numbers but who has the time for that, right?

    # Send message to all
    messages = twilio_client.send_bulk_disaster_messages(parsed_numbers, disaster_id)
    return [message.sid for message in messages]


@router.post("/send/list")
async def send_disaster_message_list(phone_numbers: List[str], disaster_id: str) -> str:
    twilio_client = TwilioClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER)

    message = twilio_client.send_bulk_disaster_messages(phone_numbers, disaster_id)
    return message.sid


@router.post("/send")
def send_disaster_message(phone_number: str, disaster_id: str) -> str:
    twilio_client = TwilioClient(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER)
    message = twilio_client.send_disaster_message(phone_number, disaster_id)
    return message.sid


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

