from calls_calculator.utils import parse_country_code


class PhoneNumber(object):

    def __init__(
        self,
        *,
        full_telephon_number: str,
        country_code: str = None,
    ) -> None:
        self.country_code = country_code
        if not country_code:
            self.country_code = parse_country_code(full_telephon_number)

        self.full_telephon_number = full_telephon_number

    def __eq__(self, phone_number) -> bool:
        return self.full_telephon_number == phone_number.full_telephon_number
