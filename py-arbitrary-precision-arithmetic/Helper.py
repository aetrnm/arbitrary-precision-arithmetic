def getQuadraticResidues(p: int) -> list:
    possibleRemainders = [i for i in range(1, p)]
    quadraticResidues = [num ** 2 % p for num in possibleRemainders]
    quadraticResidues = quadraticResidues[:len(quadraticResidues)//2]

    boolQuadraticResidues = [False] * p
    for index in quadraticResidues:
        boolQuadraticResidues[index] = True

    return boolQuadraticResidues
