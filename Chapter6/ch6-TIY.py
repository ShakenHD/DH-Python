#6-1
myDetails = {'name':'Daniel', 'surname':'Hockley', 'age':'22', 'city':'Jozi'}
print(f'Name: \t{myDetails["name"]}')
print(f'Sur: \t{myDetails["surname"]}')
print(f'Age: \t{myDetails["age"]}')
print(f'City: \t{myDetails["city"]}')

#6-2
favNums = {'Dan':'2', 'Jack':'4', 'Jenn':'9', 'Pete':'16', 'Sixtynine':'420'}
print(f'\nDan: \t{favNums["Dan"]}')
print(f'Jack: \t{favNums["Jack"]}')
print(f'Jenn: \t{favNums["Jenn"]}')
print(f'Pete: \t{favNums["Pete"]}')
print(f'Sixtynine: \t{favNums["Sixtynine"]}')

#6-3
print("\nOxford Dictionary Definitions:")
realDictionary = {'Dan':'Legend', 'Water':'H20', 'Float':'Used in python instead of double.'}

#6-4
for term in realDictionary:
    print(f'{term}:\t{realDictionary[term]}\n')

#6-5
rivers = {'nile':'egypt', 'river2':'africa', 'river69':'Sixtynine'}
for river in rivers:
    print(f'{river} runs through {rivers[river]}')

for river in rivers:
    print(river)

for river in rivers:
    print(rivers[river])

#6-7
hisDetails = {'name':'Jack', 'surname':'Sack', 'age':'99', 'city':'NY'}
herDetails = {'name':'Jenny', 'surname':'Sack', 'age':'1', 'city':'Jamaica'}

people = [myDetails, hisDetails, herDetails]
print(f'\n{people}\n')

for person in people:
    full_name = f"{person['name']} {person['surname']}"
    print(f'{full_name}:\n\tAge:\t{person["age"]}\n\tCity:\t{person["city"]}\n')



