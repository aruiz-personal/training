friends = ["Andrew","Angela","Valery"]
family =["Andy","Silva","Raquel"]

name = input("Enter a name: ")

if name in friends:
    print("You are a friend")
elif name in family:
    print("You are family")
else:
    print("I don't know you")