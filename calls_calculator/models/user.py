from typing import List

from calls_calculator.constants import MINUTES_FOR_FRIENDS_CALLS


class User(object):

    def __init__(
        self,
        *,
        name: str,
        phone_number,
        address: str,
        friend_phone_numbers: List,
        minutes_left_for_friends: int = MINUTES_FOR_FRIENDS_CALLS,
    ) -> None:
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.friend_phone_numbers = friend_phone_numbers
        self.minutes_left_for_friends = minutes_left_for_friends
