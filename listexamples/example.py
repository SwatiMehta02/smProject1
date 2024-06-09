# l1 = [1, 2, 3, 4]
# add = [i for i in l1 if i < 3]
# print(add)
#
# l2 = "Swati Mehta"
# print([i for i in l2 if i not in ['a', 'e', 'i', 'o', 'u']])

age = int(input("Age"))
age_type = None
# if age<18:
#     age_type = "Youth"
# elif age>=18 and age<60:
#     age_type = "Adult"
# else:
#     age_type = "old"

age_type = "youth" if age<18 else "Adult" if age in range(18,60) else "Old"
print(age_type)



l1 = [
    1,
    2,
    3,
    "swati"
]

for ele in l1:
