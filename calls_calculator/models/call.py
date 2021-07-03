import math


class Call(object):

    def __init__(
        self,
        *,
        charged_user,
        not_charged_user,
        start_time,
        duration: int,
        is_reverse_charge: bool = False,
    ) -> None:
        self.charged_user = charged_user
        self.not_charged_user = not_charged_user
        self.start_time = start_time
        self.duration = duration
        self.is_reverse_charge = is_reverse_charge

    @property
    def charged_user_number(self):
        return self.charged_user.phone_number

    @property
    def not_charged_user_number(self):
        return self.not_charged_user.phone_number

    @property
    def duration_in_minutes(self) -> int:
        return math.ceil(self.duration / 60)

    @property
    def type(self):
        from calls_calculator.calculators.factory import CalculatorFactory
        _all_type_calculators = CalculatorFactory.ALL_CALCULATORS
        for _type, calculator in _all_type_calculators:
            if calculator.is_calls_calculatorlicable(self):
                return _type
