n=int(input("enter the  end digit number "))
i=n
a=0
while(i<100):
    print(i)
    i=i+10
    a=a+1
print "number of values ended with %d in 1 to 100 is %d" %(n,a)
'''
enter the  end digit number 5
5
15
25
35
45
55
65
75
85
95
number of values ended with 5 in 1 to 100 is 10
'''
'''
n=int(input("enter the  end digit number "))
i=n
while(i<=100):
    if(i%10==n):
        print(i)
        i+=1
    else:
        i+=1
print "number of values ended with %d in 1 to 100 is %d" %(n,a)
'''
