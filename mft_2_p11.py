#practice 11

my_list=[["apple","apricat"],["watermelon","cucumber"],["cherry","pomegranate"]]
MyList=[]
index=0
for elem in my_list:
    MyList.insert(index,(f"{my_list[index]} orange"))
    index+=1

print(MyList)

