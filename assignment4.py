import time
import random


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def iterfibo(n):
    number_list = []
    if n <= 1:
        number_list.append(n)
    else:
        number_list = [0, 1]
        for i in range(n):
                number_list.append(number_list[i] + number_list[i + 1])
    result = number_list[n]
    return result


while True:
    nbr = int(input("Enter a number: "))
    # nbr = random.randint(30,40)
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)= %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=     %d, time %.6f" %(nbr, fibonumber, ts))