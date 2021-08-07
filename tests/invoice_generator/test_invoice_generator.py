from calls_calculator.invoice_generator.invoice_generator import \
    InvoiceGenerator


def test_get_movements(
    charged_user,
    national_call,
    international_call,
    friend_call,
    friend_call_more_minutes,
):
    """
    Test if the movements are being correctly created
    """
    calls = [
        national_call,
        international_call,
        friend_call,
        friend_call_more_minutes,
    ]

    invoice_generator = InvoiceGenerator(
        user=charged_user,
        calls=calls,
    )
    movements = invoice_generator._get_movements()

    assert len(movements) == 4
    for index, movement in enumerate(movements):
        call = calls[index]
        assert movement.destination_number == call.charged_user_number
        assert movement.duration == call.duration
        assert movement.date == call.start_time


def test_get_international_minutes(
    charged_user,
    national_call,
    international_call,
    friend_call,
    friend_call_more_minutes,
):
    """
    Test if the international minutes are being correctly calculated
    """
    calls = [
        national_call,
        international_call,
        friend_call,
        friend_call_more_minutes,
    ]

    invoice_generator = InvoiceGenerator(
        user=charged_user,
        calls=calls,
    )

    international_minutes = invoice_generator._get_total_international_minutes()
    assert international_minutes == 2


def test_get_national_minutes(
    charged_user,
    national_call,
    international_call,
    friend_call,
    friend_call_more_minutes,
):
    """
    Test if the national minutes are being correctly calculated
    """
    calls = [
        national_call,
        international_call,
        friend_call,
        friend_call_more_minutes,
    ]

    invoice_generator = InvoiceGenerator(
        user=charged_user,
        calls=calls,
    )

    national_minutes = invoice_generator._get_total_national_minutes()
    assert national_minutes == 2


def test_get_friends_minutes(
    charged_user,
    national_call,
    international_call,
    friend_call,
    friend_call_more_minutes,
):
    """
    Test if the friends minutes are being correctly calculated
    """
    calls = [
        national_call,
        international_call,
        friend_call,
        friend_call_more_minutes,
    ]

    invoice_generator = InvoiceGenerator(
        user=charged_user,
        calls=calls,
    )

    friends_minutes = invoice_generator._get_total_friends_minutes()
    assert friends_minutes == 335


def test_generate(
    charged_user,
    national_call,
    international_call,
    friend_call,
    friend_call_more_minutes,
):
    """
    Test if the invoice is being correctly created
    """

    calls = [
        national_call,
        international_call,
        friend_call,
        friend_call_more_minutes,
    ]

    invoice_generator = InvoiceGenerator(
        user=charged_user,
        calls=calls,
    )
    invoice = invoice_generator.generate()
    assert invoice.user_name == charged_user.name
    assert invoice.user_address == charged_user.address
    assert invoice.total_fees == 42.5
    assert invoice.total_international_minutes == 2
    assert invoice.total_national_minutes == 2
    assert invoice.total_friends_minutes == 335
