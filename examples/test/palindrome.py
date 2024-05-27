def is_palindrome(num):
    original=num
    reverse=0
    while num>0:
        rem=num%10 #3 2 4 7
        reverse=reverse*10+rem #3 32 324 3247
        num=num//10 #742 74 7 0
    if reverse==original:
        return True
    else:
        return False

