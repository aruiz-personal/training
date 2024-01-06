friends = ["Friend 1", "friend 2", "Friend 3"]

for friend in friends:
    print(friend)

for _ in friends:
    print("Hello world")

for index in range(2,20,3):
    print(index)


friends2= [
    {"name":"Rolf","grade":"90"}
]

for friend in friends2:
    print(friend["name"])

# Example of destructuring:
friends3 = [("Rolf",25),("Andrew",33)]

for name,age in friends3:
    print(f"Name: {name}, Age: {age}")

# Iterating over dictionaries

friends4 = {"Rolf": 23,"Andrew":33}

for name in friends4:
    print(name)

for age in friends4.values():
    print(age)

for name,age in friends4.items():
    print(f"{name},{age}")

# Break and cotinue
    
cars = ["ok","ok","faulty","ok"]

for status in cars:
    if status == "faulty":
        print("Stop")
        break
    print(status)

for status in cars:
    if status == "faulty":
        print("Skip")
        continue
    print(status)