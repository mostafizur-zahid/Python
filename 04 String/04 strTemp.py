
stri1 = "This is "
stri2 = "This is not"
name1 = "Mostafizur"
name2 = "Zahid"

temp = "This is a {} and he is good boy named {}".format(name1,name2)
print(temp)

# {} start alwasy 0 index
temp = "This is a {0} and he is good boy named {1}".format(name1,name2)
print(temp)

temp = "This is a {1} and he is good boy named {0}".format(name1,name2)
print(temp)

# or
temp = f"This is {name1} and he is good boy named {name2}"
print(temp)