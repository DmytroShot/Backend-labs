with open('input_6.txt', 'r') as file:
    data_list=file.readlines()


xyz_data="XYZ"

def getPoints(data):

    win_data="CAB"
    my_index , oponent_index = getIndexes(win_data,data)

    if(my_index==oponent_index):
        return 6 + my_index+1 # win
    
    draw_data="ABC"
    my_index , oponent_index = getIndexes(draw_data,data)

    if(my_index==oponent_index):
        return 3 + my_index+1 # draw
    
    return my_index+1 # lose
    
    
def getIndexes(combination,data):
    
    oponent_index = combination.index(data.split(" ")[0])
    my_index = xyz_data.index(data.split(" ")[1][0])
    
    return my_index , oponent_index

res = 0

for data in data_list:
    res+=getPoints(data)
    
print(res)
