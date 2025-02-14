file = open('../lab_02/input_2.txt','r')
lines = file.readlines()
data=[]


def is_safe(list):
    direction=""
    if(list[0]-list[1]>0):
        direction="up"
    else:
        direction="down"

    for i in range(len(list)-1):
        
        res=list[i]-list[i+1]
        if(direction=="up" and res<=0):
            return False
        elif(direction=="down" and res>=0):
            return False
    
        res=abs(res)
        if(res > 0 and res < 4):
            pass
        else:
            return False
    return True

res=0

for line in lines:
    for num in line.split():
        data.append(int(num))
    if(is_safe(data)):
        res+=1
    data.clear()

print(res)