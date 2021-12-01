import math
from copy import deepcopy


def toArray(value: str) -> list:
    arr = [0] * BigNumber.capacity
    length = math.ceil(len(value) / 2)
    if len(value) % 2 == 1:
        value = '0' + value
    arr_index = 0
    for i in range(length - 1, -1, -1):
        arr[arr_index] = int(value[i * 2:(i + 1) * 2])
        arr_index += 1
    return arr


class BigNumber:
    base = 100
    maxInputDecNumberLength = 10 ** 4
    capacity = maxInputDecNumberLength // 2 + 1

    def __init__(self, value: str):
        self.length = math.ceil(len(value) / 2)
        negative = value[0] == '-'
        if negative:
            self.arr = toArray(value[1:])
            self.twosComplement()
        else:
            self.arr = toArray(value)

    def __add__(self, secondNumber):
        carry = 0
        ans = BigNumber('0')
        for i in range(BigNumber.capacity):
            that = self.arr[i] + secondNumber.arr[i] + carry
            ans.arr[i] = that % BigNumber.base
            carry = that // BigNumber.base

        return ans

    def __sub__(self, secondNumber):
        secondNumberCopy = deepcopy(secondNumber)
        secondNumberCopy.twosComplement()
        return self + secondNumberCopy

    def __mul__(self, secondNumber):
        ans = BigNumber('0')
        a = deepcopy(self)
        b = deepcopy(secondNumber)
        aLength = BigNumber.capacity
        bLength = BigNumber.capacity

        for i in range(aLength):
            for j in range(bLength):
                if i + j < BigNumber.capacity:
                    ans.arr[i + j] += a.arr[i] * b.arr[j]

        for i in range(BigNumber.capacity - 1):
            ans.arr[i + 1] += ans.arr[i] // BigNumber.base
            ans.arr[i] %= BigNumber.base
        ans.arr[-1] %= BigNumber.base

        return ans

    def __truediv__(self, divisor: int):
        # truediv: 5/2 == 2.5
        pass

    def __floordiv__(self, divisor: int):
        # floordiv: 5//2 == 2
        return self.divideOnInteger(divisor)["div"]

    def __mod__(self, divisor: int) -> int:
        # mod: 5 % 2 == 1
        return self.divideOnInteger(divisor)["mod"]

    def divideOnInteger(self, divisor: int) -> dict:
        curA = 0
        ans = BigNumber('0')
        for i in range(BigNumber.capacity - 1, -1, -1):
            curA = 100 * curA + self.arr[i]
            ans.arr[i] = curA // divisor
            curA %= divisor
        return {"div": ans, "mod": curA}

    def __str__(self) -> str:
        if self.arr[-1] > 49:
            ans = deepcopy(self)
            ans.twosComplement()
            strToReturn = '-' + ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(ans.arr)).lstrip('0')
        else:
            strToReturn = ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(self.arr)).lstrip('0')
        if strToReturn == '':
            return '0'
        else:
            return strToReturn

    def twosComplement(self):
        for i in range(BigNumber.capacity):
            self.arr[i] = BigNumber.base - 1 - self.arr[i]

        self.increment()

    def increment(self):
        carry = 1
        i = 0
        while carry == 1 and i < len(self.arr):
            carry = (self.arr[i] + 1) // BigNumber.base
            self.arr[i] = (self.arr[i] + 1) % BigNumber.base
            i += 1
