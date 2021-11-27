import copy
import math
import typing


class BigNumber:
    maxNumberLength = 1000
    negativeness = False
    base = 100

    def __init__(self, value: str, negativeness: bool = False) -> None:
        self.arr = [0] * BigNumber.maxNumberLength
        self.length = len(value)
        self.negativeness = negativeness
        arr_index = 0
        for i in range(self.length - 1, -1, -2):
            self.arr[arr_index] = int(value[max(i - 1, 0): i + 1])
            arr_index += 1

    def __add__(self, secondNumber):
        carry = 0
        ans = BigNumber('0')
        for i in range(BigNumber.maxNumberLength):
            that = self.arr[i] + secondNumber.arr[i] + carry
            ans.arr[i] = that % BigNumber.base
            carry = that // BigNumber.base

        return ans

    def __sub__(self, secondNumber):
        a = copy.deepcopy(self)
        b = copy.deepcopy(secondNumber)
        aSmallerThanB = False
        if a < b:
            a, b = b, a
            aSmallerThanB = True

        if b.negativeness:
            return a + b

        carry = 0
        ans = BigNumber('0')
        aLength = math.ceil(self.length / 2)
        bLength = math.ceil(secondNumber.length / 2)
        for i in range(max(aLength, bLength)):
            that = a.arr[i] - b.arr[i] - carry
            if that < 0:
                that += BigNumber.base
                carry += 1
            else:
                carry = 0
            ans.arr[i] = that

        if aSmallerThanB:
            ans.negativeness = True
            return ans
        else:
            return ans

    @typing.overload
    def __mul__(self, secondNumber):
        ans = BigNumber('0')
        aLength = math.ceil(self.length / 2)
        bLength = math.ceil(secondNumber.length / 2)

        for i in range(aLength):
            for j in range(bLength):
                ans.arr[i + j] += self.arr[i] * secondNumber.arr[j]

        for i in range(BigNumber.maxNumberLength - 1):
            ans.arr[i + 1] += ans.arr[i] // BigNumber.base
            ans.arr[i] %= BigNumber.base

        if self.negativeness != secondNumber.negativeness:
            ans.negativeness = True
        return ans

    def __mul__(self, number: int):
        pass

    def __str__(self) -> str:
        if not self.negativeness:
            strToReturn = ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(self.arr)).lstrip('0')
            return '0' if strToReturn == '' else strToReturn
        elif self.negativeness:
            return '-' + ''.join('0' + str(x) if x < 10 else str(x) for x in reversed(self.arr)).lstrip('0')

    def __eq__(self, secondNumber) -> bool:
        return self.arr == secondNumber.arr and self.negativeness == secondNumber.negativeness

    def __gt__(self, secondNumber) -> bool:
        if self.negativeness != secondNumber.negativeness:
            return not self.negativeness and secondNumber.negativeness

        if not self.negativeness and not secondNumber.negativeness:
            if self.length != secondNumber.length:
                return self.length > secondNumber.length

            for i in range(self.length, -1, -1):
                if self.arr[i] > secondNumber.arr[i]:
                    return True
            else:
                return False

        if self.negativeness and secondNumber.negativeness:
            if self.length != secondNumber.length:
                return self.length < secondNumber.length

            for i in range(self.length, -1, -1):
                if self.arr[i] < secondNumber.arr[i]:
                    return True
            else:
                return False
