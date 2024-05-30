room_details = {
    "block": "J",
    "number": 12,
    "flat": 1004,
    "rooms": None
}

print(room_details)

room_details["furnished"] = True
room_details["rooms"] = 2
room_details.update({"rooms": 1, "gate": 1})
# delete element from dictionary
del room_details["number"]
print(room_details)

# # in operator
# print(12 in room_details)
#
# for i in room_details:
#     print(i, ":", room_details[i])

# print(room_details.get("block"))

# dict1 =dict()
# print(dict1)

# print(type(room_details.keys()))

# for i in room_details.keys():
#     print(i,":",room_details.get(i))

# print(room_details.values())
# print(room_details.items())

# for i in room_details.items():
# print(i[0], i[1])
