from keypad import constantList, functionList
import calcFunctions

actualConstants = [
    '3.141592',
    '3E+8',
    '340',
    '1.5E+8',
]

connectionWithConstants = {key: value for (key, value) in zip(constantList, actualConstants)}


def connectionWithFunctions(n):
    actualFunctions = [
        calcFunctions.factorial(n),
        calcFunctions.decToBin(n),
        calcFunctions.binToDec(n),
        calcFunctions.decToRoman(n),
    ]
    return {key: value for (key, value) in zip(functionList, actualFunctions)}

