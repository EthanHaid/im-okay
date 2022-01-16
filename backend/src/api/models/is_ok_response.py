from enum import Enum


class IsOkResponse(str, Enum):
    TRUE = "True"
    NO_RESPONSE = "No Response"
    FALSE = "False"
