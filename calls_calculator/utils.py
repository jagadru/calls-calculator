import re

from calls_calculator.constants import COUNTRY_CODE_REGEX


def parse_country_code(full_telephon_number: str) -> str:
    return re.split(COUNTRY_CODE_REGEX, full_telephon_number)[1]
