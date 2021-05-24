
amount=int(raw_input())
print "total bill is",amount
if(amount>=1000):
  c=(amount*10)/100
  print "Discount on the bill amount is",c
elif(amount>2000):
  c=(amount*20)/100
  print "Discount on the bill amount is",c  
elif(amount>3000):
  c=(amount*30)/100
  print "Discount on the bill amount is",c
elif(amount>5000):
  c=(amount*40)/100
  print "Discount on the bill amount is",c
