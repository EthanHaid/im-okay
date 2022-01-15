from fastapi import APIRouter
from ..helpers import twilio_client
from fastapi import FastAPI, File, UploadFile
from typing import List
import csv

router = APIRouter(prefix="/message")


@router.post("/send/csv")
async def send_disaster_message_csv(file: UploadFile = File(...)):
    # Parse list of numbers from CSV
    file_contents = await file.read()
    parsed_numbers = file_contents.split(',')
    # TODO: Validation for actual numbers but who has the time for that, right?

    # Send message to all
    messages = twilio_client.send_bulk_disaster_messages(parsed_numbers, "FAKE DISASTER")
    return [message.sid for message in messages]


@router.post("/send/list")
async def send_disaster_message_list(phone_numbers: List[str]) -> str:
    message = twilio_client.send_disaster_message(phone_numbers, "FAKE DISASTER")
    return message.sid


@router.post("/send")
def send_disaster_message(phone_number: str) -> str:
    message = twilio_client.send_disaster_message(phone_number, "FAKE DISASTER")
    return message.sid


@router.post("/custom")
def send_custom_message(phone_number: str, message: str) -> str:
    message = twilio_client.send_message(phone_number, message)
    return message.sid


