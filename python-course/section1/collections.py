# Lists

friends = ["Andres", "Thaly"]

print(len(friends))

friends.append("Jose")

# Tuples

tuple = ("1", "2", "3")  # brackets are optional

print(tuple)
# You can not append but you can do:

tuple2 = tuple + ("4",)

print(tuple2)

# Sets.. unordered, no repeated values/no duplicates.

art_friends = {"Rolf", "Anne"}

science_friends = {"Ralph", "Charly"}

art_friends.add("Jose")

science_friends.remove("Ralph")

# set operations
# Friends that are in art but not in science.
art_bu_not_science = art_friends.difference(science_friends)

# los que no estan en ambos
not_in_both = art_friends.symmetric_difference(science_friends)

# los que estan en ambos

both = art_friends.intersection(science_friends)

all = art_friends.union(science_friends)

# Dictionaries:

friends = (
    {"name": "Andres", "age": 33},
    {"name": "Adam", "age": 24}
)

print(friends[0]["name"])


# Convertir una lista de tuplas en un diccionario.

friends2 = [("Andres", 33), ("Jose", 24)]

friends_to_dict = dict(friends2)

print(friends_to_dict)

# len y sum

grades = [80, 75, 90, 100]

total = sum(grades)

length = len(grades)

avg = total/length

# Join list elements

friends3 = ["Andres", "Jose", "Smith"]
friends3_join = ", ".join(friends3)

print(friends3_join)
