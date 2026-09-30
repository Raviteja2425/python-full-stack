"""
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

#usage of %d,%f,%s
#Print(usage of %(args))
price=45.356;grade='A';stock=15
print("%d"%price)
print("%.1f"%price)
print("%s"%grade)


#Area of circle when radius is 3.5cm,round off the area to decimal values;
#take pi value as 3.1416

radius=float(input("enter the radius: "))

radius=3.1416*(radius **2)
print("Area of circle is %.2f"%radius)


#New style Formating -->Fstring
name="Codegnan";batch="PFS6"
print(f'{batch} is in {name}')
"""
#Control block statements--> They control the flow of the program
#Conditional statement(If,elif,else)
#Repetition statements(Loops) (for,while)
#Jumping statements(break,continue,pass)

'''
Syntax for conditional statement
'''
name=input("Enter your name: ")
weight=int(input("Enter your weight in  kgs: "))
height=float(input("Enter your height in meters: "))
bmi=(weight)/((height)**2)
if bmi<18.5:
    print(f'BMI of {name} is {bmi} and you are Underweight -->Eat well')
elif bmi>=18.5 and bmi<=24.9:
    print(f'BMI of {name} is {bmi} and you are Healthyweight --> keep consistency')
elif bmi>25 and bmi<=29.9:
    print(f'BMI of {name} is {bmi} and you are Over weight -->Start Exercising')
else:
    print(f'BMI of {name} is {bmi} and you are Obbese')





