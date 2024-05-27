from palindrome import is_palindrome

num=input()
# try:
#     print(is_palindrome(int(num)))
# except Exception as ex:
#     print(ex)

try:
    # if is_palindrome(int(num)):
    #     print("we got this")
    # else:
    #     print("we did not get it")
    print("we got this" if is_palindrome(int(num)) else "we did not get this")
except Exception as invalid:
    print(invalid)