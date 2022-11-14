#practice 8
Num=input("Enter Number =>>  ")
Num=Num.split()
# print(Num)
ListNum=[]
rangee=0
for elem in Num :
    ListNum.append(int(elem))
    rangee+=1
# print(ListNum)
ANum=sum(ListNum)
print(ANum)


