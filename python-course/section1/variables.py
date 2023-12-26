#Numbers:

float_division = 12 / 5

print(float_division)

integer_division = 12 // 5

print(integer_division)

remainder_of_a_division = 5 % 2

print(remainder_of_a_division)

#Strings:

string_variable = "Hello world!"

multi_line = """
Hello
World!
"""

print(multi_line)

#It can be use as a comment as well:
"""
This is like a comment because we are doing nothing with the string variable that is created
here. hehe
"""

#Concat:

x = "Hello"

age = 33

print(x+" Andres, you are "+str(age))

#Format:

print(f"You are {age}")

name="Andres"
final_greeting="How are you, {name}?"

andres_greeting = final_greeting.format(name=name)
print(andres_greeting)

# Bool

print(bool(0))

print(bool(""))

print(bool({}))

# Lists

friends = ["Andres", "Thaly"]

print(len(friends))

friends.append("Jose")

# Tuples

tuple = ("1","2","3") # brackets are optional

print(tuple)
#You can not append but you can do:
tuple2 = tuple + ("4",)

print(tuple2)

# Sets.. unordered, no repeated values/no duplicates.

art_friends = {"Rolf","Anne"}

science_friends = {"Ralph","Charly"}

art_friends.add("Jose")

science_friends.remove("Ralph")