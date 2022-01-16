from twilio.rest import Client
from typing import List

from api import config


DISASTER_MSG = f"""
Hey my broski, you good? 👀

Reply YES or NO
"""


class TwilioClient:
    def __init__(self, account_sid: str, auth_token: str, twilio_phone_number: str):
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_bulk_disaster_messages(self, phone_numbers: List[str], disaster_id: str):
        messages = []
        for phone_number in phone_numbers:
            messages.append(self.send_disaster_message(phone_number, disaster_id))

    def send_disaster_message(self, phone_number: str, disaster_id: str):
        message_body = f"{DISASTER_MSG}\n{config.FRONTEND_URL}?d={disaster_id}&p={phone_number}"
        return self.send_message(phone_number, message_body)

    def send_message(self, phone_number: str, message_body: str):
        message = self.client.messages.create(
            to=phone_number,
            from_=self.twilio_phone_number,
            body=message_body
        )
        return message

    def has_number_been_messaged(self, phone_number: str) -> bool:
        # TODO: Can optionally specify the specific disaster
        messages = self.client.messages.list(
            from_=self.twilio_phone_number,
            to=phone_number,
            limit=20
        )
        return len(messages) > 0
