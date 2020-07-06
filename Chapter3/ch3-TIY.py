#GUEST

guestList = ["Aden", "Salman", "Laam"]
for x in guestList:
    print(f"Hey {x}, you are invited to my dinner!")

print(f"Unfortunately, Laam can't make it, but Jacob can.")

guestList.remove("Laam")
print(guestList)

guestList.append("Jacob")
print(guestList)

for x in guestList:
    print(f"Hey {x}, you are invited to my dinner!")

print("We have reserved a larger table! I can now invite 3 more guests. Peter, Thomas and Nthando")

guestList.insert(0, "Peter")

guestList.insert(3, "Thomas")

guestList.append("Nthando")

for x in guestList:
    print(f"Hey {x}, you are invited to my dins dins!")

print("SH!T, table won't arrive in time. Gotta cancel the 4 least liked persons' invites.Get Rekt")

numGuests = len(guestList)
print(numGuests)

for x in range(1,numGuests):
    if len(guestList) > 3:
        guestList.pop()
        print(guestList)
        print(len(guestList))

for x in guestList:
    print(f"Hey {x}, you are invited to my dins dins dins dinssssssssss!")




