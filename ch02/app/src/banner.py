def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner(input("What is your message?: "))
