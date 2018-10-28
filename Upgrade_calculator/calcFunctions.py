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
    except:
        return 'Error!'
    # MMMCMXCIX = 3999
    result = 0
    for i in range(len(romanNum)):
        n = 0
        print(i)
        if i+1 <= len(romanNum)-1:
            if (romanNum[i] + romanNum[i+1]) in romanLetters:
                index = romanLetters.index(romanNum[i])
                n = romans[index][0] * (-1)
            else:
                index = romanLetters.index(romanNum[i])
                n = romans[index][0]
        else:
            index = romanLetters.index(romanNum[i])
            n = romans[index][0]

        result += n


    return str(result)
