with open('input_5.txt', 'r') as file:
    data_list=file.readlines()

def getColorSum(data,color):
    color_count = data.count(color)
    data=data.split(color)
    res = 0
    for i in range(color_count):
        res += int(data[i].split(" ")[-2])
    return res

def getGameId(data):
    data = data.split()
    index = data.index("Game")
    return data[index+1][:-1]

total_res=0

for data in data_list:
    
    blue_count = getColorSum(data,"blue")
    green_count = getColorSum(data,"green")
    red_count = getColorSum(data,"red")

    if(blue_count<=14 and green_count<=13 and red_count<=12):
        total_res += int(getGameId(data))

print(total_res)