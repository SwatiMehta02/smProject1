# x = int(input())
# y = int(input())
#
#
# def even_num(num1, num2):
#     a=[]
#     for i in range(num1, num2+1):
#         if i % 2 == 0:
#             a.append(i)
#     return a
#
#
# print(even_num(num1=x, num2=y))
#
#


# def divide_num(x, y, z):
#     a = []
#     for i in range(x, y+1):
#         if i % z == 0:
#             a.append(i)
#     return a
#
#
# x1 = int(input("first num "))
# y1 = int(input("second num "))
# z1 = int(input("third num "))
# print("divisible", divide_num(x1, y1, z1))


def count_char(word, character):
    count = 0
    for i in list(word):
        if i == character:
            count += 1
    print(count)


# a = input("string:")
# b = input("enter any character:")
# count_char(a,b)
#

def count_vowels(word):
    count = 0
    # vowels = ['a', 'e', 'o', 'u', 'i']
    for i in list(word):
        # if i == 'a' or i == 'e' or i == 'i' or i == 'u' or i == 'o':
        if i not in ['a', 'e', 'o', 'u', 'i']:
            count += 1
    return count


x = input("enter any word:")

print(count_vowels(x))
