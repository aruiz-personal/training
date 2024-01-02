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