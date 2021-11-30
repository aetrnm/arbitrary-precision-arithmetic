from BigNumberCreator import createBigNumber

with open('input.txt') as f:
    contents = f.readlines()

inputValue1 = contents[0].strip()
inputValue2 = contents[1].strip()
num1 = createBigNumber(inputValue1)
num2 = createBigNumber(inputValue2)

# print(num1.arr)
# print(num2.arr)

print(num1 * num2)
