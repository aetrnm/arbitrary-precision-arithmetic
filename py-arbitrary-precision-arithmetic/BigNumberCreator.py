import re
from BigNumberTwosComplement import BigNumber


class InvalidValueError(Exception):
    """Raised when the input value is invalid"""
    pass


def stringContainsValidNumber(string):
    pattern = re.compile('^[-+]?\\d*$')
    return pattern.match(string)


def createBigNumber(inputValue):
    if stringContainsValidNumber(inputValue):
        return BigNumber(inputValue)

    raise InvalidValueError('Entered number is invalid!')
