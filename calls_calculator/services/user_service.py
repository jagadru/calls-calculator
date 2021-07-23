from typing import Dict, List

import requests

from calls_calculator.constants import (BASE_USER_SERVICE_URL,
                                        USER_INFORMATION_RESOURCE)
from calls_calculator.exceptions import NotFoundUserException
from calls_calculator.models.telephon_number import PhoneNumber
from calls_calculator.models.user import User


class UserService:

    @classmethod
    def _get_user_information(cls, phone_number: str) -> Dict:
        _url = '{base_url}{resource}{phone_number}'.format(
            base_url=BASE_USER_SERVICE_URL,
            resource=USER_INFORMATION_RESOURCE,
            phone_number=phone_number,
        )
        response = requests.get(_url)
        return response.json() if response.ok else {}

    @classmethod
    def get_user_information(cls, phone_number: str):
        user_information = cls._get_user_information(phone_number)
        if not user_information:
            raise NotFoundUserException

        _phone_number = PhoneNumber(full_telephon_number=phone_number)

        friend_list = [
            PhoneNumber(full_telephon_number=number)
            for number in user_information.get('friends', [])
        ]  # type: List

        user = User(
            name=user_information.get('name', ''),
            phone_number=_phone_number,
            address=user_information.get('address', ''),
            friend_phone_numbers=friend_list,
        )

        return user
