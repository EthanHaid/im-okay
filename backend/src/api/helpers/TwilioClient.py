from twilio.rest import Client
from typing import List

from api import config
from ..routes.disaster import handle_create_disaster_response, _get_disaster
from ..models import DisasterResponseInput, IsOkResponse

DISASTER_MSG = f"""
Hey my fam, you good? 👀
"""


class TwilioClient:
    def __init__(self, account_sid: str, auth_token: str, twilio_phone_number: str):
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_bulk_disaster_messages(self, phone_numbers: List[str], disaster_id: str):
        messages = []
        info = _get_disaster(disaster_id)

        message = ''
        location_str = ''
        for item in info:
            k, v = item.__dict__['item']
            if k == 'message':
                message = v
            if k == 'location_string':
                location_str = v

        for phone_number in phone_numbers:
            messages.append(self.send_disaster_message(phone_number, disaster_id, message, location_str))
        return messages

    def send_disaster_message(self, phone_number: str, disaster_id: str, message: str = '', location_str: str = str):
        # Create an unanswered Disaster Response Input
        disaster_response_input = DisasterResponseInput(
            is_ok=IsOkResponse.NO_RESPONSE,
            phone_number=phone_number,
        )
        disaster_response_id = handle_create_disaster_response(disaster_id, disaster_response_input)['name']

        # Send text message
        message_body = f"{DISASTER_MSG}\nWe Heard there was a {message} near {location_str}! Click the following link to let us know you're ok!\n" \
                       f"\n{config.FRONTEND_URL}/status?disaster_id={disaster_id}&disaster_response_id={disaster_response_id} "
        print(message_body)

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
