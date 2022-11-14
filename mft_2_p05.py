#practice 5
#دو خط ورودی بگیرد 
#با ستاره جدا کند 
#دو لیست را یکی کند 
print("Hi welcome")
print("Enter your list and put stars between the items on your list")
MyList =[]
for _ in range(2):
    fruits = input().split("*")
    MyList.extend(fruits)




print(MyList)
