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
        elif parse[0] == 'del':
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
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    if scdb:
        for p in sorted(scdb, key=lambda person: person[keyname]):

            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')

            print()
    else:
         print("정보가 없습니다.")


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
