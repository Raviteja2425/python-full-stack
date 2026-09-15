"""
#input from user --> input() --> can accept any type --> result --> str.

name=int(input("Enter the temp:"))
print(name)
print(type(name))


#split--> Comma seperated 
name=input("Enter the name:").split(',')
print(name)
print(type(name))
print(len(name))


num=int(input("Enter the number:"))
print(num)
print(type(num))

#Every built-in datatype is a built-in function --> Functions --> Objects.

#Usage of map() -->  group of integer.
numbers=list(map(int,input("Enter a number: ").split(',')))
print(numbers)
print(type(numbers))
print(len(numbers))


#Usage of map() -->  group of float.
temp=list(map(float,input("Enter a temp: ").split(',')))
print(temp)
print(type(temp))
print(len(temp))


#Accept multiple values --> integers.
temperature,pressure=map(float,input("Enter the values:").split(','))
print("Temperature is",temperature)
print("Pressure is",pressure)
"""

