from datetime import datetime
from typing import List


class Movement(object):

    def __init__(
        self,
        *,
        destination_number,
        duration: int,
        date: datetime,
        fees: float,
    ):
        self.destination_number = destination_number
        self.duration = duration
        self.date = date
        self.fees = fees


class Invoice(object):

    def __init__(
        self,
        *,
        user_name: str,
        user_address: str,
        movements: List,
        total_fees: float,
        total_national_minutes: int,
        total_international_minutes: int,
        total_friends_minutes: int,
    ) -> None:
        self.user_name = user_name
        self.user_address = user_address
        self.movements = movements
        self.total_fees = total_fees
        self.total_international_minutes = total_international_minutes
        self.total_national_minutes = total_national_minutes
        self.total_friends_minutes = total_friends_minutes
