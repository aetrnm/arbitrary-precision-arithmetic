import math
from copy import deepcopy


def to_array(value: str):
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
            self.arr = to_array(value[1:])
            self.twos_complement()
        else:
            self.arr = to_array(value)

    def __add__(self, secondNumber):
        carry = 0
        ans = BigNumber('0')
        for i in range(BigNumber.capacity):
            that = self.arr[i] + secondNumber.arr[i] + carry
            ans.arr[i] = that % BigNumber.base
            carry = that // BigNumber.base

        return ans

    def __sub__(self, secondNumber):
        second = deepcopy(secondNumber)
        second.twos_complement()
        return self + second

    def __str__(self) -> str:
        if self.arr[-1] > 49:
            ans = deepcopy(self)
            ans.twos_complement()
            strToReturn = '-' + ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(ans.arr)).lstrip('0')
        else:
            strToReturn = ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(self.arr)).lstrip('0')
        if strToReturn == '':
            return '0'
        else:
            return strToReturn

    def twos_complement(self):
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
