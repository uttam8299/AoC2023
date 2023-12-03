import re

numDict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0
}

class pair:
    def __init__(self, word, index):
        self.word = word
        self.index = index


def convertWordToNum(line):
    listadd = []
    for key in numDict:
        for i in re.finditer(key, line):
            listadd.append(pair(key, i.start()))   

    listadd = sorted(listadd, key=lambda x: x.index)
    tempstr = ''
    for pr in listadd:
        tempstr += str(numDict.get(pr.word))
    return tempstr

# Actual logic goes here
def calculate(line):
    line = convertWordToNum(line) # part 2
    i = 0
    j = len(line) - 1
    result = 0
    leftNo = 0
    rightNo = 0
    while(i <= j):
        if line[i].isdigit():
            leftNo = int(line[i])
            break
        i += 1
    i = 0
    j = len(line) - 1
    while i <= j:
        if line[j].isdigit():
            rightNo = int(line[j])
            break
        j -= 1
    
    return ((leftNo * 10) + rightNo)

# code to read file and calculate
file = open('./input.txt','r')
count = 0
res = 0
while True:
    count += 1
    line = file.readline()
    if not line:
        break
    res += calculate(line)
print(res)
file.close()