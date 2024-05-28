from dict_utils import room_details

# print("This flat has",room_details["rooms"],"number of rooms")
print("Flat details are as below:")
print("\tNumber of rooms:",room_details.get("rooms","NA"))
print("\tBlock:",room_details.get("block","NA"))
print("\tRoom No:",room_details.get("flat",1001))
