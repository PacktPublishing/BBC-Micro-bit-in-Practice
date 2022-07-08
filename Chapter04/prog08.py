def factorial(number):
    if number < 0:
        print("The number must be greater than zero.")
        return -1
    elif ((number - int(number)) > 0):
        print("The number must be a positive integer.")
        return -1
    elif (number == 0) or (number == 1):
        return 1
    else:
        return number * factorial(number-1)

factorial(-1)
factorial(1.1)
print(factorial(0))
print(factorial(1))
print(factorial(5))