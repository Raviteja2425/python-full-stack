"""
name=[]
weight=[]
height=[]
for i in range(5):
    name1=input("Enter your name: ")
    weight1=int(input("Enter your weight in  kgs: "))
    height1=float(input("Enter your height in meters: "))
    bmi=(weight1)/((height1)**2)

    name.append(name1)
    weight.append(weight1)
    height.append(height1)
    if bmi<18.5:
        print(f'BMI of {name1} is {bmi} and you are Underweight -->Eat well')
    elif bmi>=18.5 and bmi<=24.9:
        print(f'BMI of {name1} is {bmi} and you are Healthyweight --> keep consistency')
    elif bmi>25 and bmi<=29.9:
        print(f'BMI of {name1} is {bmi} and you are Over weight -->Start Exercising')
    else:
        print(f'BMI of {name1} is {bmi} and you are Obbese')


print("Names:",name)
print("weights:",weight)
print("height:",height)



#Exception Handling -->
#Exception is a mechanism to a program which respond to run time errors or compliation...
#Exception --> It tries to make our program go in a Normal flow...

'''
try,except,finally....
#for every try except is mandatory...
try:
    .................
except:
    ............
finally:
    ....................

    '''


try:
    a,b=map(int,input("Enter the values:").split(','))
    result=a/b
    print(result)
except Exception as e:
    print(e)

#In above case we will get ValueError,ZeroDivisionError......
#Possible type errors --> TypeError,ValeError,NameError...
#IndexError,ZeroDivisionError,AttributeError,ArthmeticError.....


try:
    a,b=map(int,input("Enter the values:").split(','))
    result=a/b
    print(result)
except ValueError:
    print("Make sure you enter int")
except ZeroDivisionError:
    print("Make sure to givee denominator greater than zero")

"""

try:
    a=[1,2,3,4,5]
    print(a[0])
    a.append('Codegnan')
    print(a)
except (IndexError,NameError,AttributeError)as e:
    print(e)
finally:
    print("Done")






















