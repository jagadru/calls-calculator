import pytest

from calls_calculator.exceptions import NotFoundUserException
from calls_calculator.services.user_service import UserService


def test_user_created_successfully(mock_user_service):
    phone_number = '+5492612514258'

    user = UserService.get_user_information(phone_number)

    assert user.name == 'Myrna Hermann IV'
    assert user.phone_number.full_telephon_number == phone_number
    assert user.address == '2040 Dorris Prairie'
    assert user.friend_phone_numbers


def test_raise_error_no_user_information(mock_empty_user):
    phone_number = '+5492612514258'

    with pytest.raises(NotFoundUserException) as exc:
        UserService.get_user_information(phone_number)

    assert exc
