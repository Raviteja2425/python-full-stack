"""
Price of product -->5000
Discount -->10%
GST -->18%

Final Price of the Product?

INput-->Price,Discount,GST
Output-->final price
Logic-->



Price=int(input('Enter the price : '))
Discount=float(input('Enter the discount in between 0.1 - 0.2:'))
Gst=0.18

final_price=(Price - (Price*Discount))
final_price=final_price+(final_price*Gst)
print("Final Price is :",final_price)


#Operators --> Arthmetic,Assignment,Comparison,Membership,Logical,Identity,Bitwise..

#Assignment --> = (assigning), += (Update the value)

price=2500
price+=500
print (price)


# Comparision --> COmpare the value <,>,<=,>=,==,!=
# membership-->in,not in -->checks for the values in a collection

Prices=[15000,2000,13000,25000,35000]
final_price=[]
#price<=15000 10%
#price>=5000 --> 0%
#price>20000 --> 15%

#get the final prices in the list
for price in Prices:
    if price <=15000 and price > 5000:
       price = price - (price * 10 / 100)
       final_price.append(int(price))
    elif price >=20000:
       price= price - (price * 15/100)
       final_price.append(int(price))
    elif price < 5000:
        final_price.append(price)
print(final_price)



# A teacher wants to build and update a simple list of student marks.

### Important in programming : 1).Input 2).Output 3).Logic

marks=[]
for mark in range(3):
    mark=int(input("Enter the marks : "))
    marks.append(mark)
#print(marks)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
print(marks.pop())
print("Final list is ",marks)
print("Length of the list is ", len(marks))




numbers=[20,50,75,98,65,45]
print("Sorted list is: ")
numbers.sort()
print("Desc order of list is ")
numbers.reverse()
print(numbers)
num=int(input("Enter your number: "))
if num in numbers:
    print("count is",numbers.count(num))
    print("First Index is ",numbers.index(num))
else:
    print("number not found")
"""

numbers=[10,15,20,25,30,35]
even=[]
odd=[]

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

print("First 3 elements",numbers[:3])
print("Last 3 elements",numbers[-3:])
f = numbers.copy()
numbers.clear()
print("original list",numbers)
print("backup",f)











    
