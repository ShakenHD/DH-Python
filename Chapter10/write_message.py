filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('\nI love programming.')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())