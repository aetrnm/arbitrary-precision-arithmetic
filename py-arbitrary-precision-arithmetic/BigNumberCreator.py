import re
from BigNumberTwosComplement import BigNumber


def stringContainsValidNumber(string):
    pattern = re.compile('^[-+]?\\d*$')
    return pattern.match(string)


def createBigNumber(inputValue):
    if stringContainsValidNumber(inputValue):
        return BigNumber(inputValue)

    raise Exception('Entered number is invalid!')
