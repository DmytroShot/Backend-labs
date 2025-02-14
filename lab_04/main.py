with open('input_4.txt', 'r') as file:
    data=file.readlines()

def check_dir(dir_name):
    final_res=0
    res=0
    count=0

    start_index=data.index("$ cd "+dir_name+"\n")
    data[start_index]="$"
    
    for i in range(start_index+2,len(data)):
        
        symbol = data[i].split()

        if(symbol[0] == "$"):
            break

        if(symbol[0] == "dir"):
            count1,final_res1,res1=check_dir(symbol[1])
            res+=res1
            final_res+=final_res1
            count+=count1

        if(symbol[0].isdigit()):
            res+=int(symbol[0])

    print(res,dir_name)
    
    if(res<=100000):
        final_res+=res
        count+=1
    return count,final_res,res

count,final_res,res=check_dir("/")

print("count: ",count)
print("final res: ",final_res)

