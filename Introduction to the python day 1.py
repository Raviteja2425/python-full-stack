"""Introduction to the python day 1

What is program ?
Program is procces of instruction given by the user to planning what to do and how to do.

user_en = 2000
bal_ = 10000
result = bal_ - user_en 
print(result)

procedural language 

An procedural language is organized mainly on functions 

eg- c 

def cal_ad(ab):
 return a+b

a=7 
b=9 
any = cal_ad(a,b)
print(any_)

Object Orinented Programming 

OOPS is organized mainly on classes and objects 

eg - Python 
num = 7 
print (type(num))

what is python 

python is high level language 
---->python take care about memory allocation
	num = 7
	print (type(num))
	print (id(num))

  
interpreter language 
----> Python executes code line by line 
	num = 9 
	num_2=90
	print(num)
	print(type(num))
	print(id(num))

dynamically typed language 
----> No need to mention the type of data passing to the variable.
eg- 
num = 78
any_ = ['python']
nums = [1,2]
all_ = (1,2)
print(type(num))
print(type(any_))
print(type(nums))
print(type(all_))

Why Python ?
More Libraries 
cross-platforms
open-sourse
Simple syntax

Application 
used Data science 
Web development 
AI
ML
Deep Learning 

It was started early 1980's and released in the year 1991 by Guido Van Rossum.
And he picked the name from the most loved series called monty python's circus...
The frist version was released in the year 1991 which is python 0.9.0 and now we are using 3.14...

Tokens
-------- 
----> Tokens are the smalledt unit in the python.

1.Identifier is a name of variable or function or class...
 
 Variable

 num='python'
 print(type(num))

 Functions
 
 def add_(a,b):
    print(a+b)
    add_(4,5)
 
 Class 
 
 class details:
	pass
	per_1=details
	
2.Keywords 
-----------
 Keywords are already saved in python for an specified reason to run.
 ex:
 if 
 else
 for 
 while
 return
 print
 elif
 
3.Literals
-----------
---->Literals are the data types that need to be stored in Variables....
ex:
Num=90
name='ravi'

4.Operators 
------------
----> +,-,=,/,*

5.Statements 
-------------
----> Statements are the instruction given to the program...
ex:
Num = 90 

age = 19
if age >= 18
   print(age)

6.Comments
-----------
----> Once comments were open the lines inside will never execute in python..

Single line comment (#):
--> This is used to comment only one line 
ex:
  age=20 
  if age>=18: # this check age is greater or equal
  print(age)
double line comments (''' ''', """ """"):
--> Used to comment more than one line 

Variable rules
--------------
Cons 
--> Cant use number at 1st Position 
--> Dont use special char anywhere 
--> Dont use space 
--> key words 
eg: 
2num=90
$num=89
n um=88
if = 67
pros
--> Small and Capital Letters , (_) under 
eg:
Num = 90
num_1 = 87
ravi_teja = 46 

Swapping
 ex:
a, b = 45,67 
print('a=',a)
print('b=',a)

print('a=',a)
print('b=',a)

Datatypes and type conversions 
-------------------------------

1.Numeric Datatypes 
--------------------
-->Float and int are called as Numerical Datatypes.
Float:
A number which contains decimal values are called as Float datatypes.
eg:56.89
Integer(Int):

2.String
---------
--> String is a sequence of char taht are enclosed in ' '," ",""" """....
String is immutable
eg:
any_ = 'python is a computer Language'
all_ = 'Ab,&[)-+'

3.List
--------
--> List is a collection of different datatypes and it is represented by [] that are sperated by , ...
-->inside the list we call it as items
-->List is Mutable
eg:
any_ = [1,2,3,4(5,6)]
for item in any_:
    print (item)

4.Tuple
--------
-->Tuple is collection of different datatypes taht are enclosed in () and those are seperated by ,.
-->it is immutable.
eg:
nums=(09,24.25,'python',[3,4],(8,9))
5.Dictionary
------------
-->A dictionary stores data as key-value pairs.keys and vaalues are seperated by : ...
key and value pairs are also called as items and this items are seperated by , ...
Dict is represented using {}...
In keys place we can use immutable datatypes.
In value place we can use any data.
eg:
data_ = {1,2,
         name:'Teja',
         (2,3):'tuple'}
    print(data_)

6.Set
------
--> A set stores a collection of unique values.
Set does not allow any duplicate values.
Set is represented by {} and the elements are sperated by ,...
eg:
an={1,2,3.4}
print(an)

TYPE CONVERTIONS:
-----------------
float----> int,str
eg:
int()
price=45.67
print(int(price))

str()
price=45.44
con = str(price)
print(type(con))

integer---->float,str
eg:
float()
num=78
printa(float(num))

str()

num=78
con=str(num)
print(type(con))

String ----> int,float

eg:
int

do='10'
print(int(do))

float
do='10.9'
print(float(do))

list----> Tuple, string
eg:
nums=[1,2,3,4]
print(tuple(nums))

Tuple ----> List()
eg
all_=(5,6,7)
print(tuple(all_))

Set----> tuple,list

eg:
tuple()
all={5,6,7}
print(tuple(all_))

Dict ----> List
eg:
list()
Details=[('name','teja',('edu','b.tech')]

concatination:
--------------
-->The + will behave  two ways for numerics it works normally
Such as for other datatypes like string,list,tuple it place the values side by side.

Operators
----------
-->The operators are used to perform operations in variqables and the values.
1.Arthematic operators
+,-,*,/,//,%
eg:
Addition
num=90
num_2=9
print(num+num_2)

Sub
num=90
num_2=9
print(num-num_2)

Multiply
num=90
num_2=9
print(num*num_2)

Division
num=90
num_2=9
print(num/num_2)

2.Assignment operators:
------------------------
-->=,+=,-=,*=,/=
eg:
+=
n=9
n +=24
print(n)

-=
n=9
n -=24
print(n)

*=
n=9
n *=24
print(n)

/=
n=25
n /=5
print(n)

//=
n=268.5
n //=5
print(n)

3.comparison operators
-----------------------
--> ==, >=,<=,<,>,!=
a=24
b=25
print(a==b)
print(a!=b)
print(a<b)
print(a>b)

4.Logical operators
--------------------
and -->
or-->
not-->
5.identify operators:
---------------------
is
is not
eg:
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
in , not in

in->
----
nums = 'python is language'
print('y' in nums)

not in
------
nums = 'python is language'
print('i' not in nums)

7.Bitwise operator
------------------
5---> 0101
3---> 1100
1---> 0001

&---> Bitwise and
------------------
print(5&#)

|-->Bitwise or
----------------
5--->0101
3--->0011
7--->0111
print(5|3)

^--->Bitwise xor
-----------------
5-->0101
3-->0011
6-->0110
print(5^3)

>>-->Bitwise Right shift
------------------------
5-->0101
1-->0001

print(5>>2)

<<-->Left shift
5-->0101
10-->

input farmating
---------------
integet-->int(input())
----------------------
a = int(input('Enter a integer: '))

float-->float(input())
----------------------
b = float(input('enter any decimal: '))
print(b + 7)

string-->input()
-----------------
a = input('Enter a string: ')
print(type(a))

list-->list(map(int,(input().split())))
---------------------------------------
nums = list(map(int,(input('Enter some numbers: ').split())))
print(nums)

tuple-->tuple(map(int,(input().split())))
------------------------------------------
nums = tuple(map(int,(input('Enter some numbers: ').split())))
print(nums)

---->
data_ = eval()



--->eg
-------
name = 'vamsi'
age = 22

print('my name is',name,'age is',age)
print('hello!',name)

print(f'my name is {name} and i am {age} years old')

eg--->
---
name = 'vamsi'
age = 23

print('my name is %s and ia am %d years old'%(name,age))

operations:
-----------
1.Indexing:
-->Indexing is used to get char that you looking to access.
!.Positive indexing
--------------------
-->Positive indexing start from 0 index.
Syntax-->print(variable_name[index_position])
         print(text[3])
2.Negitive Indexing
--------------------
-->Negitive indexing starts from -1.
Syntax-->print(variable_name[negitive index_postion])
         print(text[-3])
-->Len():
    len() is a built-in fuction that is used to get number of char present in the string.
    syntax-->len(variable_name)
eg:
text='python is a programming language'
len(text)

Slicing:
-->This is used to a particular part from the string.
Syntax-->Variable_name[start:end]
eg:text='python is a programming language'
print(text[12:23])
print(text[12:])
print(text[:23])
print(text[::-2])

txt="madam"
txt=txt[::-1]

upper():
-->Used to convert all small char in cap.
eg:text='python is a programming language'
   print(text.upper())

lower():
--------
-->used to convert all cap into small
eg:text='python is a programming language'
   print(text.lower())

index():
-->used to know the index position of a char.
syntax-->variable_name.index('substring')
eg:
text='python is a programming language'
print(text.index('l'))

replace():
----------
-->used to replace the old substring with new substring.
syntax--variable_name.replace(old'substring',new'substring')
eg:
text='python is a programming language'
print(text.replace('python','java'))

split():
-------
-->this method is used to seperate the string based on the given substring.
syntax-->
text='Python is a programming language'
print(text.split(' '))

Count()
-------
-->used to count the number of occurrence of a substring.
eg:
text='Python is a programming language'
print(text.count('p'))

Indexing:
---------
postive-->0
Negitive-->-1
eg:
so=[1,2,3,4,'python']
print(so[-1][5])
all_= [12,[1,'python',[1,4],(78,[6,7])],['java',78]]
print(all_ [1][3][1])

eg:
data=['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(data[1][2][1][2])

len():
------
-->The function is used to find the number oof items present inside the list.
syntax-->len(variable_name)
eg:
data = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]

print(len(data))

Slicing:
--------
-->
data=[1,2,3,4,5,6,7]
print(data[2:6])

adding two lists:
a=[1,2]
b=[3,4]
print(a+b)

--->Methods:-
   ---------- 
append():
---------
-->append method is used will add new items into the list at last index position.
syntax-->variable_name.append(item)

go=[1,2]
print(go)
go.append(4)
print(go)

extend():
---------
-->extend() will add the items into a list at last index possition,but it will give each value as one index inside list.
syntax-->variable_name.extend(items)
eg
--
a=[1,2]
a.extend('python')
print(a)

pop():
------
pop() is used to remove items from the list and it will delete based on the index position.
syntax-->variable_name.pop(index_position)
eg:
a=[1,2,3]
a.pop(2)
print(a)

remove():
---------
-->

Tuple:
-------
-->Tuple is collection of different data types that seperated by,and represented by ()
-->immutable.
--> We can pass a tuple of values that can be asign to the variables,but should match same number of variables and values insidethe tuple.
eg:t=(1,'python',[3,4],(7,9))

indexing:
-->If items is not present in the tuple,it will raise ValueError.

eg:
--
t=(1,'python',[3,4],(7,9))
print(t.index('python'))

len()

max()
-----
-->used to find out highest value from the tuple.
eg
so=(67,34,53)
print(max(so))

min()
-----
-->used to find out least value from the tuple.
eg:
so=(67,34,53)
print(min(so))

count()
-------
-->used to count an item present in tuple.
eg
--
so=(67,54,453,4342,45,3)
print(so.count(5))

sets:
-----


union():
--------
-->The union() will combine two sets into a single set.
And wew use | this symbol.
Syntax-->set_1.union(set_2) or (set_1 | set_2)
eg:
data = {1,2,3,4}
nums={5,6}
print(data.union(nums))
print(data | nums)

intersection():
---------------
-->This will give us the common elements from both sets.
we can use & symbol.
syntax-->set_1.intersection(set_2) or (set_1 & set_2)
eg:
data = {1,2,3,4}
nums={4,5,6}
print(data.intersection(nums))
print(data & nums)

difference():
-------------
-->It will display different elements from set_1,but not from the other set.
we can use - symbol.
syntax-->set_1.difference(set_2) or set_1 - set_2
eg:
---
data = {1,2,3,4}
nums={4,5,6}
print(data.difference(nums))
print(data - nums)

symmetric_difference():
------------------------
-->Different elements from the both sets.
we can use ^ symbol.
syntax-->set_1.symmetric_difference(set_2) or set_1 ^ set_2

add():
------
-->add method will add only one element at a time.
syntax-->set_1.add(value)
eg:
data = {1,2,3,4}
data.add(7)
print(data)

update():
---------
-->we can add more than one element by using update method.
syntax-->set_1.unpdate([values]) or set_1,update(set_2)
eg:
data = {1,2,3,4}
nums={4,5,6}
data.update([8,7])
print(data)
data.update(nums)
print(data)

remove():
---------
-->Remove() method will delete the given value from the set.if the element does not exist then it will give error.
syntax-->set.remove(value)
eg:
data = {1,2,3,4}
nums={4,5,6}
data.remove(3)
print(data)

Discard():
----------
-->Discard() method is used to del the elemnt from the set ,but never raise any error if the element does not exist in the set.
syntax-->set.discard(value)
eg:
data = {1,2,3,4}
nums={4,5,6}
data.discard(8)
print(data)
data.discard(2)
print(data)

clear():
--------
-->The method is used to delete all the values and it will return empty set.
syntax-->set.clear()
eg:
data = {1,2,3,4}
print(data)
data.clear()
print(data)

Dictionary():
-->A dictionary stores data as key-value pairs.keys and vaalues are seperated by : ...
key and value pairs are also called as items and this items are seperated by , ...
Dict is represented using {}...

Accessing:
----------
-->Dict can be access by calling key,we will get value from that key.
syntax-->dict['key']

get():
-->get method also used to get the value from that key.
syntax-->dict.get(key).
eg:
data ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}

print(data['name'])
print(data['balance'])
print(data['adr'])
print(data['PANC'])
print(data.get(2))

update():
---------
-->update method is used to update a key,if the key does not exisit in the dict then it add that key:value
syntax-->dict.update({key:value})

There is an another way to update a key
syntax-->dict[key]=value.
eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data)
data['AC']=4587651684618

data.update({'name':'sony'})
print(data)

Values():
---------
-->values() method is used to get all values from the dict.
syntax-->print(dict.values())

eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data.values())

keys():
--------
-->keys method is used to retrive all the keys from dict.
syntax-->print(dict.values())

eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data.keys())

items():
--------
-->the method will get the key value pair seperately from the dict.
syntax-->dict.items()
eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data.items())

clear():
--------
-->clear method is used remove entire data from a dict.
syntax-->dict.clear()
eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data)
data.clear()
print(data)

del():
-------
--> This method is used delete a key-value pair from dict.
syntax-->del dict.[key]

eg:
data = {'name':'teja',
        'balamce':700000,
        'adr':1234567890,
        'panc':'GPXBP2980V',
        2:[3,4]}
print(data)
del data['adr']
print(data)

If statement:
-------------
-->If condition become true,then it will execute inside stock of code.
-->Incase it becomes false,then it will never entry inside blocks.

eg:
a=90
b=78
if a>b:
    print(a)

elif:
-----
-->elif statement is used to check more possible outcomes or more conditions.
eg:
a=90
b=890
c=67

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

eg:
num =7
num_2=67
user_opt=int(input('Enter \n1.add \n2.sub \n3.mul \n4.pow: '))
if user_opt==1:
    print(num+num_2)
elif user_opt==2:
    print(num-num_2)
elif user_opt==3:
    print(num*num_2)
else: 
    print(num**num_2)

nested if:
----------
--> If inside an if statement is called nested if.
eg:
app_details={'pin':4500}           
import random
user_pass=int(input("Enter your password: "))
otp=random.randint(1000,9999)
if user_pass==app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp=int(input('Enter 4 digit otp: '))

    if user_otp==otp:
        print('Welcome to the app')
    else:
        print('entered otp is incorrect')
        
else:
    print('password is incorrect')

eg:
a=int(input('Enter a number: '))
if a % 2==0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

For loop:
----------
-->for loop is used to iterate over a sequence or iterable datatypes.

eg:
---
nums=[12,3,4,13]
for num in nums:
    print(num)

else in for:
------------
-->unlike if-else,else block in for statement is executed after completed for all iterations.

eg:
---
nums=[12,3,4,13]
for num in nums:
    print(num)
else:
    print('for ended')


break:
------
-->the break statement used to stop iteration based on the condition given.
eg:
---
nums=[1,2,3,4,5]
for num in nums:
    if num==3: 
     print(num)
     break

continue:
---------
-->the continue is keyword is used to skip current iteration based on the condition.

eg:
val=[1,2,3,4,5,6,7,8659]
for j in val:
    if j == 5:
       continue
    print(j)

pass:
-----
-->A pass is a spaceholder ,that is used after statements like (if,for,else) not to raise any error.

assert:
-------
-->assert is a keyword used to check the condition,in case the condition is false ,it will raise the error(AssertionError)
eg:
age=15
assert age >=18,'not eligible to vote'
print('Your eligible to vote')

eg:
limit_ = int(input("Enter a number: "))

for i in range(2, limit_ + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(f'{i} is prime')



word ='python'
empty_str=''
for k in word:
    empty_str=k+empty_str
    print(empty_str)

        
word ='madam'
empty_str=''
for k in word:
    empty_str=k+empty_str
if empty_str ==word:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not palindrome')

eg:
num = int(input('Enter a number:'))
length=len(str(num))
amstrong_=0
for i in str(num):
    amstrong_=amstrong_+int(i)**length
    print(amstrong_)
if amstrong_==num:
    print(f' {num} is amstrong')
else:
    print(f'{num} is not amstrong')

eg:
n = int(input('Enter a number='))

sum = 0

for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum == n:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')


FUnction:
==========
-->A function is block of code that can be executed only when is called...
-->A function start with def keyword and the line called as defination line,where we can define a fun_name.
--> And if we want to execute the program in the function,need to call with the function name define at def line.

Syntax-->
def fun_name(parameters):
    pass
function_name(argument)

eg:
---
def add_ (a,b):
    print(a+b)
add_(5,6)

Arguments:
===========
Positional argument:
-->The arguments should be same at def line and calling,incase if they are not same number will raise an error.

num = 0
num_1 = 1
print(num,num_1,end=' ')
for i in range(1,10):
    num_2 = num + num_1
    num = num_1
    num_1 = num_2
    print(num_2,end=' ')

default argument:
-----------------
-->The default arguments where the function will only consider the data at calling function,even though the data present at def line.
eg:
---
def feb_(num,num_2):
    print(num+num_2)
feb_([1,3][5,6])

eg:
---
def data_(a=8,b=9):
    print(a+b)
data_(1,5)

eg:

def prime(num=10,count=1):
    for i in range(2, num + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            print(f'{i} is prime')
        else:
            print(f'{i} is not prime')
prime(num=int(input("Enter a number: ")),count=0)

keyword arguments:
==================
-->Keyword arguments are sending argument in pair(a=2),
and pass order is not consider...
eg
--
def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name='teja',age=45,location='vizag',batch=6)

Variable length argument:
==========================
-->Adding a (* call is as args) before a variable define at parameters.
we can pass tuple of arguments.

eg:
def all_(*name):
    print(name)
all_('teja','45','vizag','6')

keyword length argument:
=========================
-->def details(**data_):
    print(data_.keys())
details(Name='teja',age=45,location='vizag',batch=6)

return:
=======
-->Return keyword is used insed the function,once the return is exected
means it will get back to calling with return values.
eg:
---

"""

def all_(a,b):
    return a-b
print(all_(7,9))





































