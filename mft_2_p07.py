#pracyice 7
#سوال-> جمله را از ورودی بگیرید  کلمه آخر و اول  را چاپ کنید و بقیه جمله را هم چاپ کنید
sentences = input("Hello\nYou can type your sentence here ")

sentences=sentences.split()
# print(sentences)
FirstWord=[]
FirstWord=sentences.pop(0)
# print(FirstWord)
LastWord=[]
LastWord=sentences.pop(-1)
# print(LastWord)
# print(sentences)
print(f"first word =>{FirstWord}\nLast Word=>{LastWord}\nrest=>{sentences}")