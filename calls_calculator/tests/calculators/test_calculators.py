from calls_calculator.calculators.fees import (FriendFeesCalculator,
                                               InternationalFeesCalculator,
                                               NationalFeesCalculator)


# Tests for NationalFeesCalculator
def test_national_fee_calculator_is_calls_calculatorlicable(national_call):
    assert NationalFeesCalculator.is_calls_calculatorlicable(national_call)


def test_national_fee_calculator_is_not_calls_calculatorlicable(international_call):
    assert not NationalFeesCalculator.is_calls_calculatorlicable(international_call)


def test_national_fee_calculator_calculate_fee(national_call):
    assert NationalFeesCalculator.calculate_fees(national_call) == 2.5


# Tests for InternationalFeesCalculator
def test_international_fee_calculator_is_calls_calculatorlicable(international_call):
    assert InternationalFeesCalculator.is_calls_calculatorlicable(international_call)


def test_international_fee_calculator_is_not_calls_calculatorlicable(national_call):
    assert not InternationalFeesCalculator.is_calls_calculatorlicable(national_call)


def test_international_fee_calculator_calculate_fee(international_call):
    assert InternationalFeesCalculator.calculate_fees(international_call) == 20.0


# Test for FriendFeesCalculator
def test_friend_fee_calculator_is_calls_calculatorlicable(friend_call):
    assert FriendFeesCalculator.is_calls_calculatorlicable(friend_call)


def test_friend_fee_calculator_is_not_calls_calculatorlicable(international_call):
    assert not FriendFeesCalculator.is_calls_calculatorlicable(international_call)


def test_friend_fee_calculator_calculate_fee(friend_call):
    assert FriendFeesCalculator.calculate_fees(friend_call) == 0.0


def test_friend_fee_calculator_calculate_fee_national_call(friend_call_more_minutes):
    assert FriendFeesCalculator.calculate_fees(friend_call_more_minutes) == 2.5


def test_friend_fee_calculator_calculate_fee_international_call(
    friend_call_more_minutes_international,
):
    assert FriendFeesCalculator.calculate_fees(
        friend_call_more_minutes_international
    ) == 6680.0
