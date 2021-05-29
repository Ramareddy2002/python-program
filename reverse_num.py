
n=int(input('enter number which you want to reverse:- '))
sum=0
a=n
while n!=0:
    r=n%10
    sum = sum*10+r
    n=n//10
print("reverse of %d is %d "%(a,sum))
'''
output is :-
enter number which you want to reverse:- 12345
reverse of 12345 is 54321 
'''
