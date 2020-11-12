#The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. 
# The ten numbers not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88. 
# Let f(n) be the count of numbers not exceeding n with exactly eight divisors. 
# You are given f(100) = 10, f(1000) = 180 and f(106) = 224427. 
# Find f(1012). 
def checker(n):
    count=0

    for i in range (1,n+1):
        if n%i==0:
            count=count+1
    return count
x=1
num=[]
while x<=1012:
    val=checker(x)
    if val==8:
        num.append(x)
    x+=1
print(len(num))