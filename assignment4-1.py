import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            print("seqsearch >>", nbrs[i], "  ", i)
            return i
    return -1


def recbinsearch(list, low, upper, target):
    middle = (upper+low)//2
    middleNum = list[middle]
    if upper == low or upper < low:
        return -1
    if target == middleNum:
        print("{}   {}".format(upper, low))
        print("binsearch >>", middleNum, "  ", middle)

        return middleNum
    elif target > middleNum:
        print("{}   {}".format(upper, low))
        return recbinsearch(list, middle+1, upper, target)
    elif target < middleNum:
        print("{}   {}".format(upper, low))
        return recbinsearch(list, low, middle-1, target)



numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 100)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 100)]


ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers)-1, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
print()
ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
print(sorted(targets))