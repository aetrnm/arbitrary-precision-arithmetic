import re
from BigNumber import BigNumber


def stringContainsValidNumber(string):
    pattern = re.compile("^[-+]?\\d*$")
    return pattern.match(string)


def createBigNumber(inputValue):
    if stringContainsValidNumber(inputValue):
        if inputValue[0] == '-':
            return BigNumber(inputValue[1:], True)
        return BigNumber(inputValue)

    raise Exception('Entered number is invalid!')


a = input()
b = input()
num1 = BigNumber(a)
num2 = BigNumber(b)
print(num1 + num2)
