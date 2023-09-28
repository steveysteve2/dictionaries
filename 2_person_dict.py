person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child

children = person['children']
print(type(children))
print(person['children'][1])

# print out the name of the cat

pets = person["pets"]
print(type(pets))
print(person['pets']['cat'])

cat_name = person['pets']['cat']
print(cat_name)


# use a loop to print out the names of each child

for child in person['children']:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for k, v in person["pets"].items():     #items method gives key and value at the same time
    print(f"The type of pet is: {k} and the name of the pet is: {v}")