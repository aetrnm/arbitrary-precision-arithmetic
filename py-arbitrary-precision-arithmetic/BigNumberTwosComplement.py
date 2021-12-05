import math
from copy import deepcopy


class BigNumber:
    base = 100
    maxInputDecNumberLength = 10 ** 4
    currentMaxInputDecNumberLength = 100

    def __init__(self, value: str):
        self.capacity = self.getCapacity()
        self.length = math.ceil(len(value) / 2)
        negative = value[0] == '-'
        if negative:
            self.arr = self.toArray(value[1:])
            self.twosComplement()
        else:
            self.arr = self.toArray(value)

    def __add__(self, secondNumber):
        carry = 0
        ans = BigNumber('0')
        for i in range(self.capacity):
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
        aLength = a.capacity
        bLength = b.capacity

        for i in range(aLength):
            for j in range(bLength):
                if i + j < ans.capacity:
                    ans.arr[i + j] += a.arr[i] * b.arr[j]

        for i in range(ans.capacity - 1):
            ans.arr[i + 1] += ans.arr[i] // BigNumber.base
            ans.arr[i] %= BigNumber.base
        ans.arr[-1] %= BigNumber.base

        return ans

    def __floordiv__(self, divisor: int):
        # floordiv: 5//2 == 2
        return self.divideOnInteger(divisor)["div"]

    def __mod__(self, divisor: int) -> int:
        # mod: 5 % 2 == 1
        return self.divideOnInteger(divisor)["mod"]

    def __pow__(self, number: int):
        a = deepcopy(self)
        for _ in range(number - 1):
            a *= self

        return a

    def toArray(self, value: str) -> list:
        # TODO: check capacity of input
        arr = [0] * self.capacity
        length = math.ceil(len(value) / 2)
        if len(value) % 2 == 1:
            value = '0' + value
        arr_index = 0
        for i in range(length - 1, -1, -1):
            arr[arr_index] = int(value[i * 2:(i + 1) * 2])
            arr_index += 1
        return arr

    def getCapacity(self):
        return self.currentMaxInputDecNumberLength // 2 + 1

    def divideOnInteger(self, divisor: int) -> dict:
        curA = 0
        ans = BigNumber('0')
        for i in range(self.capacity - 1, -1, -1):
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

    def __repr__(self):
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

    def __eq__(self, other):
        return self.arr == other.arr

    def __ne__(self, other):
        return self.arr != other.arr

    def __gt__(self, secondNumber):  # self > secondNumber
        difference = self - secondNumber
        return difference.getSign() == 1

    def twosComplement(self):
        for i in range(self.capacity):
            self.arr[i] = BigNumber.base - 1 - self.arr[i]

        self.increment()

    def increment(self):
        carry = 1
        i = 0
        while carry == 1 and i < len(self.arr):
            carry = (self.arr[i] + 1) // BigNumber.base
            self.arr[i] = (self.arr[i] + 1) % BigNumber.base
            i += 1

    def getSign(self):
        if sum(self.arr) == 0:
            return 0
        elif self.arr[-1] > 49:
            return -1
        elif self.arr[-1] <= 49:
            return 1

    def getCeilIntegerSquareRoot(self):
        if self == BigNumber('1'):
            return BigNumber('1')
        bottomBorder = BigNumber('1')
        topBorder = self // 2

        while bottomBorder != topBorder:
            middle = (topBorder + bottomBorder) // 2
            if middle ** 2 > self:
                topBorder = middle
            elif middle ** 2 < self:
                bottomBorder = middle
                bottomBorder.increment()
            elif middle ** 2 == self:
                return middle

        return bottomBorder

    def factorize(self) -> list:
        # x = (a+b)(a-b) = a**2 - b**2         17
        # a = (sqrt(x) ....)                   5
        # a**2 - x == b**2 ?                   8
        # b**2 <- full square? sqrt(b)**2 == b 3
        # x = 9 * 3 -> ans = [9, 3]
        ans = []
        a = self.getCeilIntegerSquareRoot()
        bb = a ** 2 - self
        b = bb.getCeilIntegerSquareRoot()
        while bb != b ** 2:
            a.increment()
            bb = a ** 2 - self
            b = bb.getCeilIntegerSquareRoot()
        f = a + b
        s = a - b
        if s == BigNumber('1'):
            return [f]

        for num in f.factorize():
            ans.append(num)
        for num in s.factorize():
            ans.append(num)

        return ans
