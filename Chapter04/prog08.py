def print_message(string, count):
    if (count > 0):
        print(string)
        print_message(string, count - 1)

print_message("Hello, World!", 5)
