from calls_calculator.calculators.fees import (FriendFeesCalculator,
                                               InternationalFeesCalculator,
                                               NationalFeesCalculator)
from calls_calculator.constants import FRIENDS, INTERNATIONAL, NATIONAL
from calls_calculator.types import CallInformation


class CalculatorFactory:

    ALL_CALCULATORS = (
        (FRIENDS, FriendFeesCalculator),
        (INTERNATIONAL, InternationalFeesCalculator,),
        (NATIONAL, NationalFeesCalculator,),
    )

    @classmethod
    def get_calculator_class(cls, call: CallInformation):
        for _type, calculator in cls.ALL_CALCULATORS:
            if call.type == _type:
                return calculator
