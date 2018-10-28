from keypad import constantList
import calcFunctions

actualConstants = [
    '3.141592',
    '3E+8',
    '340',
    '1.5E+8',
]

constantMap = {key: value for (key, value) in zip(constantList, actualConstants)}