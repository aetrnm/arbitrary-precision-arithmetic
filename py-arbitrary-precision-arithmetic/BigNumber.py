class BigNumber:
    maxNumberLength = 100
    negativeness = False

    def __init__(self, value: str, negativeness=False):
        self.arr = [0] * BigNumber.maxNumberLength
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

    def __str__(self):
        if not self.negativeness:
            return ''.join(map(str, reversed(self.arr))).lstrip('0')
        elif self.negativeness:
            return '-' + ''.join(map(str, reversed(self.arr))).lstrip('0')

    def __eq__(self, secondNumber):
        return self.arr == secondNumber.arr
