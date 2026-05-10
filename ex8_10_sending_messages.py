# a function called send_messages()
#   that prints each text message
#   then move each message .pop()
#   to a new list called sent_messages .append()
def send_messages(message, sent):
    """prints and move each message from a list to another"""
    while message:
        msg = message.pop(0)
        print(msg)
        sent.append(msg)


short_text_messages = [
    'Hey, just checking in. Hope your day is going well.',
    'I saw something today that reminded me of you.',
    'Do not forget to take a break and drink some water.',
    'You have been on my mind lately.',
    'Hope something good happens to you today.'
]

sent_messages = []

send_messages(short_text_messages, sent_messages)

print('\nOriginal List:')
print(short_text_messages)
print('\nSent List:')
print(sent_messages)
# after function call, print original list then new list
