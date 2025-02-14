with open('input_3.txt', 'r') as file:
    data=file.readlines()


def findNum(line):
    res=""
    for symbol in line:
        if(symbol.isdigit()):
            res+=symbol
            break
    for symbol in line[::-1]:
        if(symbol.isdigit()):
            res+=symbol
            break
    return res

res=0

for line in data:
    res+=int(findNum(line))

print(res)
