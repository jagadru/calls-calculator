from datetime import datetime
from typing import List

from calls_calculator.constants import (BILLING_PERIOD_DATETIME_FORMAT,
                                        CALL_DATETIME_FORMAT)
from calls_calculator.exceptions import NotFoundUserException
from calls_calculator.invoice_generator.invoice_generator import \
    InvoiceGenerator
from calls_calculator.models.call import Call
from calls_calculator.services.user_service import UserService


class Processor:

    def _get_user_information(self, phone_number):
        try:
            return UserService.get_user_information(phone_number)
        except NotFoundUserException as error:
            print('Error Code: {err_code}. Message: {message}'.format(
                err_code=error.code,
                message=error.message.format(phone_number),
            ))
            return

    def __init__(
        self,
        *,
        phone_number: str,
        raw_calls: List,
        billing_period: str,
    ) -> None:
        self.phone_number = phone_number
        self.raw_calls = raw_calls
        self.billing_period = datetime.strptime(billing_period, BILLING_PERIOD_DATETIME_FORMAT)
        self.user = self._get_user_information(self.phone_number)

    def _should_process(self, start_time, caller_number, destination_number):
        return all([
            start_time > self.billing_period,
            self.phone_number in [caller_number, destination_number]
        ])

    def process(self) -> None:
        self.calls = []  # type: List
        self.user = self._get_user_information(self.phone_number)

        for raw_call in self.raw_calls:
            start_time = datetime.strptime(raw_call.get('start_time'), CALL_DATETIME_FORMAT)
            caller_number = raw_call.get('caller_number')
            destination_number = raw_call.get('destination_number')

            if not self._should_process(start_time, caller_number, destination_number):
                continue

            try:
                caller = UserService.get_user_information(raw_call.get('caller_number'))
                destination = UserService.get_user_information(raw_call.get('destination_number'))
            except NotFoundUserException as error:
                print('Error Code: {err_code}. Message: {message}'.format(
                    err_code=error.code,
                    message=error.message,
                ))
                continue

            if not raw_call.get('is_reverse_charge'):
                charged_user = caller
                not_charged_user = destination
            else:
                charged_user = destination
                not_charged_user = caller

            call = Call(
                charged_user=charged_user,
                not_charged_user=not_charged_user,
                is_reverse_charge=raw_call.get('is_reverse_charge'),
                duration=int(raw_call.get('duration')),
                start_time=start_time,
            )

            self.calls.append(call)

        invoice = InvoiceGenerator(user=self.user, calls=self.calls).generate()
        print('Invoice: {}'.format(invoice.__dict__))
