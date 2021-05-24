
amount=int(raw_input())
print "total bill is",amount
c=0
if(amount<1000):
    print("sorry! No discount on your bill")
    print"u need to buy ",(1000-amount),"to get 10% discount"
if(amount>=1000 and amount<=2000):
  c=(amount*10)/100
  print "Discount on the bill amount is",c
elif(amount>2000 and amount<=3000):
  c=(amount*20)/100
  print "Discount on the bill amount is",c  
elif(amount>3000 and amount<=5000):
  c=(amount*30)/100
  print "Discount on the bill amount is",c
elif(amount>5000):
  c=(amount*40)/100
  print "Discount on the bill amount is",c
print "amount to be paid",(amount-c)
#output
'''
6000
total bill is 6000
Discount on the bill amount is 2400
amount to be paid 3600
'''
'''
333
total bill is 333
sorry! No discount on your bill
u need to buy  667 to get 10% discount
amount to be paid 333
'''
