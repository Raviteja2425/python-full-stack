a = 90
b = 78
if a > b:
    print(a)

a = 90
b = 890
c = 67
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

num = 7
num_2 = 67
user_opt = int(input('Enter 1.add 2.sub 3.mul 4.pow: '))
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
elif user_opt == 4:
    print(num ** num_2)
else:
    print('Invalid option')

app_details = {'pin': 4500}
import random

user_pass = int(input('Enter your password: '))
otp = random.randint(1000, 9999)
if user_pass == app_details['pin']:
    print('Password is correct')
    print(otp)
    user_otp = int(input('Enter 4 digit OTP: '))
    if user_otp == otp:
        print('Welcome to the app')
    else:
        print('Entered OTP is incorrect')
else:
    print('Password is incorrect')

number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')
