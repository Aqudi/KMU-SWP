from keypad import constantList

actualConstants = [
    '3.141592',
    '3E+8',
    '340',
    '1.5E+8',
]

constantMap = {key: value for (key, value) in zip(constantList, actualConstants)}

romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
]

romanLetters = [letter[1] for letter in romans]