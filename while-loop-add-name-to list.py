# to add name into an enpty list

myList=[]

while len(myList) < 5:
    new_name= input("Please what is your name?:").strip().capitalize()
    myList.append(new_name)
print("Sorry!, the list is full")
print(myList)
