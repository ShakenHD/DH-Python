#7-1
"""
car = input("Car type wanted?")
print(f"Let me see if I can find you a/n {car}!")
"""

#7-2
"""
numPeople = input("How many people for dinner?")
if int(numPeople) > 8:
    print("\nPlease wait, no table big enough ready.")
else: print("\nFollow me, your table is ready!")
"""


#7-3
"""
num = input("Please enter an integer:")
if int(num)%10 == 0:
    print("Your number is a multiple of 10.")
else: print("Your number is not a multiple of 10.")
"""

#7-4
"""
toppingsList = []
topping = ""
while topping != 'quit':
    topping = input('Which topping would you like to add? (Enter quit to quit): ')
    print(f'Adding {topping} to pizza!')
    toppingsList.append(topping)
print(f'\ntoppingsList')
"""

#7-5
"""
age = input("How old are you?")
while age != quit:
    if int(age) < 3:
        print("Your ticket is free.")
    elif int(age) < 12:
        print("Your ticket is $10.")
    else: print("Your ticket is $15.")
    age = input("How old are you?")
"""
#7-6
"""
age = input("How old are you?")
while age != 'quitConditional':
    
    if age == 'quitBreak':
        break;
        
    elif int(age) < 3:
        print("Your ticket is free.")
        
    elif int(age) < 12:
        print("Your ticket is $10.")
        
    else: print("Your ticket is $15.")
    
    age = input("How old are you?")
"""
#7-8

"""
sandwichOrders = ['tuna sandwich', 'avo sandwich', 'ham sandwich', 'pb sandwich', 'honey sandwich', 'pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich']
finishedSandwiches = []

while sandwichOrders:
    if sandwichOrders[0] == 'pastrami sandwich':
        print("We have run out of pastrami, sorry.")
        finishedSandwiches.append(sandwichOrders[0])
        sandwichOrders.remove(sandwichOrders[0])
        continue
    print(f"I made your {sandwichOrders[0]}\n")
    finishedSandwiches.append(sandwichOrders[0])
    sandwichOrders.remove(sandwichOrders[0])
    print(sandwichOrders)

print(finishedSandwiches)
"""

#7-10
flag = 'true'
places = []
while flag == 'true':
    place = input("Where would you like to go if you could visit one place in the world?")
    if place == 'quit':
        flag = 'false'
    places.append(place)
print(places)
