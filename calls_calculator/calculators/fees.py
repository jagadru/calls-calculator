from abc import ABCMeta, abstractmethod

from calls_calculator.constants import (BASE_FEE_INTERNATIONAL_CALL,
                                        BASE_FEE_NATIONAL_CALL)
from calls_calculator.types import CallInformation


class BaseFeesCalculator(metaclass=ABCMeta):
    """
    Calculator for calls.

    This class is responsible for determining the call type and fees.
    """

    @staticmethod
    @abstractmethod
    def is_calls_calculatorlicable(call: CallInformation) -> bool:
        """Return whether the rule calls_calculatorlies to this call."""

    @staticmethod
    @abstractmethod
    def calculate_fees(call: CallInformation) -> float:
        """ Return the amount of money calls_calculatorlicable to the call."""


class NationalFeesCalculator(BaseFeesCalculator):

    @staticmethod
    def is_calls_calculatorlicable(call: CallInformation) -> bool:
        return call.charged_user_number.country_code == call.not_charged_user_number.country_code

    @staticmethod
    def calculate_fees(call: CallInformation) -> float:
        return BASE_FEE_NATIONAL_CALL


class InternationalFeesCalculator(BaseFeesCalculator):

    @staticmethod
    def is_calls_calculatorlicable(call: CallInformation) -> bool:
        return call.charged_user_number.country_code != call.not_charged_user_number.country_code

    @staticmethod
    def calculate_fees(call: CallInformation) -> float:
        return BASE_FEE_INTERNATIONAL_CALL * call.duration_in_minutes


class FriendFeesCalculator(BaseFeesCalculator):

    @staticmethod
    def is_calls_calculatorlicable(call: CallInformation) -> bool:
        return call.not_charged_user_number in call.charged_user.friend_phone_numbers

    @staticmethod
    def calculate_fees(call: CallInformation) -> float:
        fee = 0.0  # type: float

        if call.charged_user.minutes_left_for_friends < call.duration_in_minutes:
            if NationalFeesCalculator.is_calls_calculatorlicable(call):
                fee = NationalFeesCalculator.calculate_fees(call)
            elif InternationalFeesCalculator.is_calls_calculatorlicable(call):
                fee = InternationalFeesCalculator.calculate_fees(call)

        return fee
