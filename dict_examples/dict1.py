details = {
    "fname": "Swati",
    "lname": "Mehta",
    "age": 24,
    "city": "Kolkata",
    "designation": "ASE"
}
# print(type(details))  # to get the class type
# index
# print(details["age"])
# print(details["fname"])
# print(details["fname"] + " " + details["lname"])
# print(len(details))# length of dict

# print(details.get("age1", 50)) # if key is not present then return None or the second argument
# print(details["age1"])

employees = [
    {
        "fname": "Swati",
        "lname": "Mehta",
        "age": 24,
        "city": "Kolkata",
        "designation": "ASE"
    },
    {
        "fname": "Swati1",
        "lname": "Mehta1",
        "age": 23,
        "city": ["Kolkata","Patna"],
        "designation": "ASE"
    },
    {
        "fname": "Swati2",
        "lname": "Mehta2",
        "age": 29,
        "designation": "ASE"
    }
]
for data in employees:
    print("full name - ", data["fname"] + " " + data["lname"])
    print("age - ", data["age"])
    print("address - ", data.get("city", "NA"))
