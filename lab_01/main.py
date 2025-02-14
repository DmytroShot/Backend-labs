list1=[]
list2=[]

file = open('../lab_01/input_1.txt','r')
data = file.readlines()

for i in range(len(data)):
    list1.append(int(data[i].split()[0]))
    list2.append(int(data[i].split()[1]))

file.close()

def find_min(list):
    min=list[0]
    for letter in list:
        if(letter<min):
            min=letter
    return min

res=0

for j in range(len(list1)):
    first_min = find_min(list1)
    second_min = find_min(list2)

    list1.remove(first_min)
    list2.remove(second_min)

    #res.append(abs(first_min-second_min))
    res+=abs(first_min-second_min)


print(res)
