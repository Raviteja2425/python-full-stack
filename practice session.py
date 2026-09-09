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

"""

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
