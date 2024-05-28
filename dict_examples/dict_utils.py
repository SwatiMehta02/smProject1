room_details = {
    "block":"J",
    "number":12,
    "flat":1004,
    "rooms":None
}

# dict1 =dict()
# print(dict1)

# print(type(room_details.keys()))

for i in room_details.keys():
    print(i,":",room_details.get(i))

print(room_details.values())
print(room_details.items())

for i in room_details.items():
    print(i[0], i[1])

