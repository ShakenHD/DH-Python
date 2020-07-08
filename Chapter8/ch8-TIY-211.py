
list_of_messages = ['hello', 'how are you?', 'I am good', 'me too']
def show_messages():
    while list_of_messages:
        print(list_of_messages[0])
        del list_of_messages[0]
show_messages()
print("\n")

sent_messages = []
list_of_messages = ['hello', 'how are you?', 'I am good', 'me too']
def send_messages():
    while list_of_messages:
        sent_messages.append(list_of_messages[0])
        del list_of_messages[0]
send_messages()
print(sent_messages)
print("\n")

list_of_messages = ['hello', 'how are you?', 'I am good', 'me too']
def send_messages_keeping_original():
    while list_of_messages:
        count = 0
        list_length = len(list_of_messages)
        print(list_of_messages[count])
        sent_messages.append(list_of_messages[count])
        count += 1

print(f'original: {list_of_messages}')
print(f'sent: {sent_messages}')
