import re
from BigNumber import BigNumber
from Exceptions import InvalidValueError


def stringContainsValidNumber(string):
    pattern = re.compile('^[-+]?\\d*$')
    return pattern.match(string)


def createBigNumber(inputValue):
    if stringContainsValidNumber(inputValue):
        return BigNumber(inputValue)

    raise InvalidValueError('Entered number is invalid!')
