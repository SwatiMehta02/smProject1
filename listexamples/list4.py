# myname = "swati mehta"
# a = [i for i in myname if i in ['a', 'e', 'i', 'o', 'u']]
# print(a)

# num1 = int(input())
# num2 = int(input())
# b = [i for i in range(num1, num2 + 1) if i in range(6, 21)]
# print(b)

x = int(input('enter x: '))
# is_even = None
divided_by = None  # 2 if divided by 2 if 3 se divide 3 else 0
# if x % 2 == 0:
#     is_even = True
# else:
#     is_even = False

# is_even = True if x % 2 == 0 else False
# print(is_even)

# if x % 2 == 0:
#     divided_by = 2
# elif x % 3 == 0:
#     divided_by = 3
# else:
#     divided_by = 0
# print(divided_by)

divided_by = 2 if x % 2 == 0 else 3 if x % 3 == 0 else 0
print(divided_by)
