""""
print("Hello world")

#perform operation as below

a=15
b=34
print(a+b)

#Tokens-->Keywords,Variables,Operators,Punchuators [],(),{}.
#The variable should not start with numbers,space,symbol,and also no spaces between words.

batch=['PFS-6','DA-6']
print(batch)
print(type(batch))

#len() --> returns the number of items in the collection..
print(len(batch))

#Add 3 more students names into it
#List --> collection --> append(),extend(),inser()..

batch.append('Ravi')
batch.extend(['subash','sandepp'])
batch.insert(0,'sai') #inserts given value at specific index
batch.insert(-1,'python')#If its negitive values add before index...
print(batch)
# Indexing --> [] --> index starts at 0 and ends at len(obj)-1
#print(batch[0])
#print(batch[34]) #IndexError --> length is only 7 we are accessing  extra.

#Slicing --> group of values [start:end]

#print(batch[ :4])
#print(batch[4:6])
#Last 3 elements --> we prefer negative index values...
#print(batch[-3:])
#print(batch[:3])
#Striding --> [start:end:step]


print(batch[::3])
print(batch[::2])
print(batch[1:5:2])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])

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
"""
#Every built-in datatype is a built-in function --> Functions --> Objects.

#Usage of map() -->  group of integer.
numbers=list(map(int,input("Enter a number: ").split(',')))
print(numbers)
print(type(numbers))
print(len(numbers))

















