list1 = [1, 2, 3, '4']  # len = 4
list2 = list()  # [] : len = 0

# length of list
print(len(list1))
print(len(list2))

list1.append(5)  # [1,2,3,4,5]
list1.append(['hello', 5, 7.6])  # [1,2,3,4,5, ['hello', 5, 7.6]]

# to find the index
print(list1)
# print(list1.index(100))
list2 = [1, 2, 3, 4, 5, 1, 3, 6, 9, 3, 1, 2, 1, 1, 5]
print(list2.index(3))
print(list2.index(3, 4))
# print(list2.index(3, 4, 5))

# remove element
list2.remove(3)
print(list2)

# pop element
list2.pop()
print(list2)

print(list2.pop(4))
print(list2)

# sort list
# list2.sort()
list2.sort(reverse=True)
print(list2)

# count number of
print(list2.count(1))



#extend function