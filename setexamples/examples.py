dict1 = {"name": "Swati", "age": 24}
for k, v in dict1.items():
    print(k, v)

for item in dict1.items():
    print(item[0],item[1])

dict1.items() # [("name","Swati"),("age",24)]
#k,v=("name","Swati")
for i in dict1:
    print(i,dict1.get(i))

dict1.keys() # ['name','age'] # dict1.get(age) #dict1.get()
for i in dict1.keys():
    print(i,dict1.get(i))
    # print(i,dict1[i])

