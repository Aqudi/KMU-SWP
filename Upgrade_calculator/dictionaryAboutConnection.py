from keypad import constantList, functionList

actualConstants = [
    '3.141592',
    '3E+8',
    '340',
    '1.5E+8',
]

connectionWithConstants = {key: value for (key, value) in zip(constantList, actualConstants)}

"""
actualFunctions = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]

connectionWithFunctions = {key: value for (key, value) in zip(functionList, actualFunctions)}

"""