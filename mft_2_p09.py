#practice 9
print("Enter Number :  ")
MyList=[]

for elem in range(4):
    MyList.append(int(input()))
MaxNum=max(MyList)
MinNum=min(MyList)
sumNum=sum(MyList)
print(f"Max Number: {MaxNum}\nMin Number: {MinNum}\nSum Number: {sumNum}")
