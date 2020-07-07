#5-1
car1 = 'Subaru'
car2 = 'BMW'
car3 = 'Toyota'
car4 = 'Merc'
car5 = 'Car5'

print("Is car1 == 'subaru'? I predict True.")
print(car1 == 'Subaru')
print("Is car2 == 'BMW'? I predict True.")
print(car2 == 'BMW')
print("Is car3 == 'Toyota'? I predict True.")
print(car3 == 'Toyota')
print("Is car4 == 'Merc'? I predict True.")
print(car4 == 'Merc')
print("Is car5 == 'Car5'? I predict True.")
print(car5 == 'Car5')

print("\nIs car1 == 'audi'? I predict False.")
print(car1 == 'audi')
print("Is car2 == 'audi'? I predict False.")
print(car2 == 'audi')
print("Is car3 == 'audi'? I predict False.")
print(car3 == 'audi')
print("Is car4 == 'audi'? I predict False.")
print(car4 == 'audi')
print("Is car5 == 'audi'? I predict False.")
print(car5 == 'audi')

#5-2
num1 = 1; num2 = 2; num3 = 3; num4 = 4; num5 = 5
name1 = 'Dan'; name2 = 'Olivia'; name3 = 'Peter'
nameList = [name1, name2, name3]

print("\nIs name1 Dan?")
print(name1 == 'Dan')

print("\nIs name1 dan?")
print(name1.lower() == 'Dan')

print("\nIs num4 > num5?")
print(num4 > num5)

print("\nIs num4 = num5?")
print(num4 == num5)

print("\nIs num4 > num5 and name1 = Dan?")
print(num4 > num5 and name1 == 'Dan')

print("\nIs num4 > num5 or name1 = Dan?")
print(num4 > num5 or name1 == 'Dan')

print(nameList)
print("\nIs Dan in the list of names?")
print('Dan' in nameList)

print("\nIs Jenny in the list of names?")
print('Jenny' in nameList)

print("\nIs Jenny not in the list of names?")
print('Jenny' not in nameList)

#5-3
alienColor = 'green'
if alienColor == 'green':
    print("correct, you score 5 points")
if alienColor == 'red':
    print("correct, you score 5 points")

#5-4
if alienColor == 'blue':
    print("\ncorrect, you score 5 points for shooting the correct alien")
else:
    print("You are dumb, wrong alien")

#5-5
if alienColor == 'blue':
    print("\ncorrect, you score 5 points for shooting the correct alien")
elif alienColor == 'green':
    print("\ncorrect, you score 5 points for shooting the 2nd correct alien")
else:
    print("You are dumb, wrong alien")

#5-6
age = 22
if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("toddler")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print("teen")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65:
    print("elder")

#5-7
favFruits = ["apples", "bananas", "grapes", "berries", "naartjies"]

if 'apples' in favFruits:
    print("\ndo you really like apples?")
if "bananas" in favFruits:
    print("do you really like bananas?")

#5-8
usernames = ['admin', 'dhoc', 'shaken', 'bobsnob', 'ilikeapples']

for userid in usernames:
    if userid == 'admin':
        print("sup admin, you the boss")
    else:
        print(f"hello {userid}, you are not the boss")

#5-9
for userid2 in usernames:
    print(usernames)
    print('aaa')
    if not usernames:
        print("We need users!")
    else:
        print(f"still {len(usernames)} users")
        usernames = []

#5-10
print(usernames)
currentUsers = ['admin', 'dhoc', 'shaken', 'bobsnob', 'ilikeapples']
newUsers = ['ADMIN', 'NEWdhoc', 'shaken', 'bobsnob', 'NEWilikeapples']

print(f"\n\n{newUsers}")
print(f"{currentUsers}\n")

for user in newUsers:
    if user in currentUsers:
        print(f"please enter a new username as {user} is already taken")
    else:
        print(f'Congrats! {user} username is available')







