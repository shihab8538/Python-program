
def reverse(x):
    if(x<0):
        x =abs(x)
        sign = -1
    else:
        sign = 1
    r=0
    while(x >0):
        a=x%10
        x=x//10
        r =(r*10)+a
        r = r *sign
        
    if r < -2**31 or r >2**31-1:
        return 0
    return r
y = reverse(3214)
print(y)