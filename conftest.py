from datetime import datetime
from unittest import mock

import pytest

from calls_calculator.models.call import Call
from calls_calculator.models.telephon_number import PhoneNumber
from calls_calculator.models.user import User


@pytest.fixture()
def mock_user_service():
    response = {
        'address': '2040 Dorris Prairie',
        'friends': [
            '+5491167920944',
            '+5491167980954',
            '+5491167980953',
            '+5491167980951',
            '+191167980953'
        ],
        'name': 'Myrna Hermann IV',
        'phone_number': '+5492612514258'
    }

    with mock.patch(
        'calls_calculator.services.user_service.UserService._get_user_information',
        return_value=response,
    ) as mocked:
        yield mocked


@pytest.fixture()
def mock_empty_user():
    with mock.patch(
        'calls_calculator.services.user_service.UserService._get_user_information',
        return_value={},
    ) as mocked:
        yield mocked


@pytest.fixture()
def charged_user():
    return User(
        name='Myrna Hermann IV',
        phone_number=PhoneNumber(
            full_telephon_number='+5492612514258',
            country_code='54',
        ),
        address='2040 Dorris Prairie',
        friend_phone_numbers=[
            PhoneNumber(
                full_telephon_number='+5491167980953',
                country_code='54',
            )
        ],
    )


@pytest.fixture()
def friend_user():
    return User(
        name='Myrna Hermann VI',
        phone_number=PhoneNumber(
            full_telephon_number='+5491167980953',
            country_code='54',
        ),
        address='2040 Dorris Prairie',
        friend_phone_numbers=[
            PhoneNumber(
                full_telephon_number='+5491167980953',
                country_code='54',
            )
        ],
    )


@pytest.fixture()
def not_charged_user():
    return User(
        name='Myrna Hermann V',
        phone_number=PhoneNumber(
            full_telephon_number='+5492612514258',
            country_code='54',
        ),
        address='2040 Dorris Prairie',
        friend_phone_numbers=[
            PhoneNumber(
                full_telephon_number='+5491267980953',
                country_code='54',
            )
        ],
    )


@pytest.fixture()
def usa_user():
    return User(
        name='Myrna Hermann V',
        phone_number=PhoneNumber(
            full_telephon_number='+192612514258',
            country_code='1',
        ),
        address='2040 Dorris Prairie',
        friend_phone_numbers=[],
    )


@pytest.fixture()
def national_call(charged_user, not_charged_user):
    return Call(
        charged_user=charged_user,
        not_charged_user=not_charged_user,
        start_time=datetime.now(),
        duration=10,
        is_reverse_charge=False,
    )


@pytest.fixture()
def international_call(charged_user, usa_user):
    return Call(
        charged_user=charged_user,
        not_charged_user=usa_user,
        start_time=datetime.now(),
        duration=10,
        is_reverse_charge=False,
    )


@pytest.fixture()
def friend_call(charged_user, friend_user):
    return Call(
        charged_user=charged_user,
        not_charged_user=friend_user,
        start_time=datetime.now(),
        duration=10,
        is_reverse_charge=False,
    )


@pytest.fixture()
def friend_call_more_minutes(charged_user, friend_user):
    return Call(
        charged_user=charged_user,
        not_charged_user=friend_user,
        start_time=datetime.now(),
        duration=20000,
        is_reverse_charge=False,
    )


@pytest.fixture()
def friend_call_more_minutes_international(charged_user, usa_user):
    return Call(
        charged_user=charged_user,
        not_charged_user=usa_user,
        start_time=datetime.now(),
        duration=20000,
        is_reverse_charge=False,
    )
