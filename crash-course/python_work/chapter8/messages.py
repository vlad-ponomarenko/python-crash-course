messages = ["a", "b", "c"]


sent_messages = []


def send_messages(messages):

    while messages:
        sent_message = messages.pop()
        print(sent_message)
        sent_messages.append(sent_message)


send_messages(messages[:])
print(messages)
print(sent_messages)
