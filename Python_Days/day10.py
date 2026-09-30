try:
    print(5 / 0)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No error occurred')

try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print('Division by zero')
else:
    print('No error occurred')

try:
    number = int(input('Enter a number: '))
    print(100 / number)
except ValueError:
    print('Please enter a valid integer')
except ZeroDivisionError:
    print('You cannot divide by zero')
finally:
    print('Program finished')
