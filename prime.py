n=int(input('enter number:'))
i=1
Count=0
if(n<2):
    print("wrong number")
else:
    while (i<(n//2)+1):
        if(n%i==0):
            Count+=1
        i+=1
    if (Count==1):
        print("%d is a prime number" %n)
    else:
      print("%d is not a prime number" %n)
'''
enter number:4
4 is not a prime number

enter number:1
wrong number

enter number:7
7 is a prime number
'''
