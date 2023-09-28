import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



# print()
# print('*****  start section 1 - print dictionary ********')
# print()

# print(phonebook)

# print(len(phonebook))

# phone = phonebook['Chris']

# print(phone)

# phonebook = {}

# mydictionary = dict(m=8,n=9)         #Function dict uses normal ()

# print(mydictionary)

# print()
# print('*****  end section 1 ********')
# print()




# print()
# print('*****  start section 2 - search dictionary ********')
# print()


# name = 'chris'

# if name in phonebook:
#     phone = phonebook[name]
#     print(phone)
# else:
#     print(f'{name} not found in phonebook')



# print()
# print('*****  end section 2 ********')
# print()





# print()
# print('*****  start section 3 - edit/append dictionary ********')
# print()

# print(phonebook)
# phonebook['Joe'] = '555-0123'       #no append command, just apply key-value pair and it adds
# phonebook['Chris'] = '555-4444'         
# print(phonebook)

# print()
# print('*****  end section 3 ********')
# print()




# print()
# print('*****  start section 4 - delete/remove from dictionary ********')
# print()

# del phonebook['Chris']
# print(phonebook)


# print()
# print('*****  end section 4 ********')
# print()


# print()
# print('*****  start section 5 - iterate through keys, values, items ********')
# print()


# for k in phonebook:           #dictionaries iterate through keys by default
#     print(f'the key is {k} and their number is: {phonebook[k]}')  #returns back a string value

# for v in phonebook.values():            #iterates through values
#     print(f'the value is {v}')

# for phone_tuple in phonebook.items():   #returns both key and values
#     print(phone_tuple)

# for k,v in phonebook.items():        #returns both key and values
#     print(f'the key is {k} and their number is: {v}')

# print()
# print('*****  end section 5 ********')
# print()


# print()
# print('*****  start section 6 - using get and clear ********')
# print()

# phone = phonebook.get('katie', '911') #add Default number to check value
# print(phone)

# phonebook.clear()       #clears out all keys and values in dictionary

# print(phonebook)


# print()
# print('*****  end section 6 ********')
# print()



# print()
# print('*****  start section 7 - using pop method ********')
# print()

# print(phonebook)
# phone = phonebook.pop('Katie', '911')
# print(phone)            #cuts out value from dictionary
# print(phonebook)


# print()
# print('*****  end section 7 ********')
# print()


# print()
# print('*****  start section 8 - using popitem ********')
# print()

# print(phonebook)
# phone = phonebook.popitem()         #randomness part does not work
# print(phone)
# print(phonebook)


# print()
# print('*****  end section 8 ********')
# print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

# phonebook_list = list(phonebook)    #creates a list of keys in your dictionary
# print(phonebook_list)

# random_key = random.choice(phonebook_list)
# print(random_key)
# print(phonebook[random_key])

print(random.choice(list(phonebook)), '\n',phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()
