import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            # check if input satisfied format and type of value
            if len(parse) == 4:
                try:
                    parse[2] = int(parse[2])
                    parse[3] = int(parse[3])
                except:
                    print("Age and Score should be integer")
                    continue
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            else:
                print("The Command 'add' should be used in the format 'add name age score'")
                continue
        elif parse[0] == 'del':
            try:
                count = 0
                for p in scdb:
                    if p['Name'] == parse[1]:
                        count += 1
            except:
                print("The Command 'del' should be used in the format 'del name'")
                continue
                # 반복문을 돌고 리스트를 초기화 해야 동일한 항목이 여러개 있어도 깨끗하게 지워진다.
            for i in range(count):
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        break
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            temp = []
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        temp += [p]
            except:
                print("The Command 'find' should be used in the format 'find name'")
                continue
            print("'{}'님의 정보({}건):".format(parse[1], len(temp)))
            showScoreDB(temp, 'Name')
        elif parse[0] == 'inc':
            if len(parse) == 3:
                temp = []
                try:
                    parse[2] = int(parse[2])
                except:
                    print("amount should be integer")
                    continue
                for p in scdb:
                    if p['Name'] == parse[1]:
                        temp += [p]
                print("'{}'님의 정보({}건):".format(parse[1], len(temp)))
                showScoreDB(temp, 'Name')
                number = int(input("점수를 더하고 싶은 사람의 번호를 입력해 주세요: "))
                temp[number - 1]['Score'] += parse[2]
            else:
                print("The Command 'inc' should be used in the format 'inc name amount'")
                continue
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    if scdb:
        for number, p in enumerate(sorted(scdb, key=lambda person: person[keyname])):
            print("{}.".format(number+1), end=' ')
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')

            print()
    else:
         print("정보가 없습니다.")


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
