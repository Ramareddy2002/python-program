def sample(x,y):
    print "a value is ",x 
    print "b value is ",y
    print "a+b =",
    return x+y
def sub(x,y):
    print "a-b =",
    return x-y
def sub2(x,y):
    print "a*b =",
    return x*y
def sub3(x,y):
    print "a/b =",
    return x/y
a=int(input())
b=int(input())
print sample(a,b)
print sub(a,b)
print sub2(a,b)
print sub3(a,b)

#OUTPUT:-
'''
45
5
a value is  45
b value is  5
a+b = 50
a-b = 40
a*b = 225
a/b = 9
'''
