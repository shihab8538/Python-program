
def isPalindrome(x):
    if(x <0):
        print(x,"Not a Palindrome number")
    else:

        y=x
        rev=0
        while(x>0):
            a=x%10
            x=x//10
            rev=(rev*10)+a
        if(rev == y):
            print(y,"Palindrome number")
        else:
            print(y,"Not a Palindrome number")
isPalindrome(-120)
isPalindrome(121)
isPalindrome(20)
isPalindrome(123454321)
