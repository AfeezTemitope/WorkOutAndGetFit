from paystacks.errors import InvalidDataError


def validate_amount(amount):

    if not amount:
        raise TypeError('Amount to be changed is required')

    if isinstance(amount, int) or isinstance(amount, float):
        if amount < 0:
            raise InvalidDataError('Amount cannot be negative')
        return amount
    else:
        raise InvalidDataError('Amount should be a number')


def validate_currency(currency):

    if not currency:
        raise TypeError('Currency cannot be None')


def validate_interval(interval):

    interval = interval if interval.lower() in ['hourly', 'daily', 'weekly', 'monthly', 'annually'] else None
    if not interval:
        raise InvalidDataError('Interval cannot be None')
    return interval


