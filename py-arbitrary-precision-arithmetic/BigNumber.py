class BigNumber:
    maxNumberLength = 1000
    negativeness = False

    def __init__(self, value: str, negativeness=False) -> None:
        self.arr = [0] * BigNumber.maxNumberLength
        self.length = len(value)
        self.negativeness = negativeness
        for i in range(len(value) - 1, -1, -1):
            self.arr[i] = int(value[len(value) - i - 1])

    def __add__(self, secondNumber):
        carry = 0
        ans = BigNumber('0')
        for i in range(BigNumber.maxNumberLength):
            that = self.arr[i] + secondNumber.arr[i] + carry
            ans.arr[i] = that % 10
            carry = that // 10
        return ans

    def __str__(self) -> str:
        if not self.negativeness:
            strToReturn = ''.join(map(str, reversed(self.arr))).lstrip('0')
            return '0' if strToReturn == '' else strToReturn
        elif self.negativeness:
            return '-' + ''.join(map(str, reversed(self.arr))).lstrip('0')

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
