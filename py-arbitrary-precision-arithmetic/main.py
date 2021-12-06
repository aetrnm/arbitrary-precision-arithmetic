from BigNumberCreator import createBigNumber
from Helper import getQuadraticResidues

with open('input.txt') as f:
    contents = f.readlines()

inputValue1 = contents[0].strip()
inputValue2 = contents[1].strip()
num1 = createBigNumber(inputValue1)
num2 = createBigNumber(inputValue2)

res = num1.factorize()
print(sorted(res))
# print(getQuadraticResidues(37))
