list1 = list()
print(len(list1))

list2 = []
print(len(list2))

print(list1 == list2)

list3 = ["swati", 1, 2, 1.2, True]
print(list3[2])
try:
    print(list3[5])
except IndexError as ex:
    print(ex)
print("asdfghjk")

list3[2] = "mehta"
print(list3)

# slicing list3[start:stop:step]
list4 = list3[1::2]
print(list4)

list5 = [2,4,8,9]
# addition operator
list5 = list5 + list3
print(list5)
# multiplication operator
list6 = list5*3
print(list6)

# remove element
del list6[2]
print(list6)

del list6[3:8]
print(list6)

list7 = [1,2,4,[1,2,3],8,9]
print(list7[3][2])

list7[3][1] = 5
print(list7)