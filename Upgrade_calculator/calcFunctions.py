from math import factorial as fact
from constant import romans, romanLetters

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result

def romanToDec(numStr):
    try:
        romanNum = str(numStr)
        for num in romanNum:
            if num not in romanLetters:
                raise ValueError #원래 INDEXERROR였는데 바꿨어
    except ValueError:
        return 'Error!'
    # MMMCMXCIX = 3999

    result = 0
    for i in range(len(romanNum)):
        n = 1
        index = romanLetters.index(romanNum[i])
        if i+1 <= len(romanNum)-1 and (romanNum[i] + romanNum[i+1]) in romanLetters:
            n = (-1)
        else:
            n = 1
        result += romans[index][0] * n
    return str(result)
