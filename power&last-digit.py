num=int(input("enter the number"))
powr=int(input("enter the power"))
if(powr<0 or num<0):
    print("invalid input")
else:
    temp=num**powr#OR pow(num,powr)
    print "%d^%d=%d" %(num,powr,temp)
    print "last digit in %d^%d is %d"%(num,powr,(temp%10))
#OUTPUT:-
'''
-------:case1:-----------
enter the number2
enter the power5
2^5=32
last digit in 2^5 is 2
-------:case2:-----------
enter the number2
enter the power-1
invalid input
'''
