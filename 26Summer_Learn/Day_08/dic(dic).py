users = {}
users["user1"] = {
    "name": "Alice",
    "age": 20,
    "location": "Singapore"
}
users["user2"] = {
    "name": "Bob",
    "age": 30,
    "location": "Japan"
}
for user, user_info in users.items():
    print(user, user_info["name"])
user1 = users["user1"]
user1["age"] = 21
print(users["user1"])
users["user2"]["location"] = "China"
print(users["user2"])
del users["user2"]["location"]
users["user2"]["new_location"] = "Hong Kong"
print(users["user2"])
user2_info = users["user2"].get("name", "Unknown")
print(user2_info)