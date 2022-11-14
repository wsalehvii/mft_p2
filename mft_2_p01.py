#practice 1 
#در یک خط 5 عدد از ورودی بگیرید 
#str->int
inputlist = input("Enter 5 Number: ")
NumList = inputlist.split()
print(NumList)
index = 0
MyList=[]
for item in NumList:
    MyList.append(int(item))
    index +=1
print(NumList)     
print(MyList)
#WsalehVII