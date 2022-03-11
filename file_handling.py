with open("new.txt","r") as f:
    lines = f.readlines()
    for line in lines :
        temp = line.split(" ")
        print(temp[0])