from typing import List

from calls_calculator.calculators.factory import CalculatorFactory
from calls_calculator.constants import FRIENDS, INTERNATIONAL, NATIONAL
from calls_calculator.models.invoice import Invoice, Movement
from calls_calculator.types import CallInformation, UserInformation


class InvoiceGenerator(object):

    def __init__(
        self,
        *,
        user: UserInformation,
        calls: List[CallInformation],
    ):
        self.user = user
        self.calls = calls

    def _get_movements(self) -> List:
        movements = []  # type: List

        for call in self.calls:
            calculator = CalculatorFactory.get_calculator_class(call)
            fees = calculator.calculate_fees(call)

            movements.append(
                Movement(
                    destination_number=call.charged_user_number,
                    duration=call.duration,
                    date=call.start_time,
                    fees=fees,
                )
            )

        return movements

    def _get_total_international_minutes(self) -> int:
        return sum([
            call.duration_in_minutes
            for call in self.calls
            if call.type == INTERNATIONAL
        ])

    def _get_total_national_minutes(self) -> int:
        return sum([
            call.duration_in_minutes
            for call in self.calls
            if call.type == NATIONAL
        ])

    def _get_total_friends_minutes(self) -> int:
        return sum([
            call.duration_in_minutes
            for call in self.calls
            if call.type == FRIENDS
        ])

    def _get_total_fees(self, movements) -> float:
        return sum([
            movement.fees
            for movement in movements
        ])

    def generate(self):
        movements = self._get_movements()

        invoice_parameters = {
            'user_name': self.user.name,
            'user_address': self.user.address,
            'movements': movements,
            'total_fees': self._get_total_fees(movements),
            'total_international_minutes': self._get_total_international_minutes(),
            'total_national_minutes': self._get_total_national_minutes(),
            'total_friends_minutes': self._get_total_friends_minutes(),
        }

        return Invoice(**invoice_parameters)
