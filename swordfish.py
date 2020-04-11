#   continue Statement example

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is the file´s name.) ')
    password = input()
    if password == 'sowrdfish':
        break
    else:
        print('Wrong!')

print('Access granted.')