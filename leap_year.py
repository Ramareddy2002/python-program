def is_leap(year):
    non_leap = False
    leap= True
    
    if(year%400==0 or(year%100!=0 and year%4==0)):
        return leap
    else:
        return non_leap # Write your logic here

year = int(input())
print(is_leap(year))
'''
1997
False
---------------------
2004
True
'''
