#practice 2
my_list =[49,0,1,-1,-49,-2]

def sort_fucntion(item):
    return abs(50-item) 


my_list.sort(key=sort_fucntion, reverse=True)
print(my_list)