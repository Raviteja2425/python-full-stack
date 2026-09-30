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


a,b=13,4.5
print(a,b,end=' ')
print("Codegnan is in vizag",end='\t')



a,b=map(int,input("Enter your number: ").split(','))
addition=a+b
subtraction=a-b
multiply=a*b
divide=a/b

print("------------------>CALCULATOR<--------------------")
print()
print("Addition result is :",addition)
print("Subtraction result is :",subtraction)
print("Multiply result is :",multiply)
print("Division result is :",divide)
print()
"""























