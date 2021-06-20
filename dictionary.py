data = {1: 'Maruf', 2: 'Khan', 4: 'Shaheb'} #Data is key:value pair
print(data)
print('index of two from the dict: ',data[2])


data = {'first_name': 'Maksudur', 'middle_name': 'Rahman', 'last_name': 'Maruf'}
print('Dictionary is: ',data)
print('when key not found:',data.get('lzast_name', 'not found')) #if key not found then show comment

#a dictionary combine of two list
key = {'Tajal', 'Maruf', 'Julfikar'}
values = {'Java', 'Python', 'JS'}

keyvalues = dict (zip(key,values))
print('Combination of list Dictionary is: ',keyvalues)
# print(keyvalues['Tajal'])

keyvalues['Sayket'] = 'Vuejs' #add key $ value into dictionary
print('after insert sayket into dictionary: ', keyvalues)

del keyvalues['Sayket']
print('after delete sayket from dict: ',keyvalues)


print('============Nested Dictionary Example============')

home = {'Tajal': 'Rajshahi',
        'Julfikar': 'Dinajpur',
        'Sayket': ['Narayngonj', 'Dhaka'], #Sayket is a list here
        'Efrana': {'home_dis': 'Brakkhonbariya', #Efrana is a dctionary here
                   'originally_from': 'Noakhali',
                   'living': 'Dhaka',
                   'future_living': 'Japan'}}

print('full dictionaary is: ',home)
print('specific value from Efrana Dictionary: ',home['Efrana']['future_living'])

