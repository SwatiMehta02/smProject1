list1 = []
x, y = 10, 100
for i in range(x,y+1):
    if i % 5 == 0:
        list1.append(i)
print(list1)


list2 = [i for i in range(x,y+1) if i%5==0]
print(list2)

list3 = [i*2 for i in range(x, y+1) if i % 2 == 0 and i % 3 == 0]
print(list3)
lista = []
list4 = []
listb = []
[lista.append(i) for i in range(x, y+1) if i % 4 == 0]
[list4.append(i) if i % 4 != 0 else listb.append(i) for i in range(x,y+1)]
print("list4:",list4)
print("listb:",listb)