name = {
    "first_name": "H",
    "second_name": ["X", "H"]
}
print(name["first_name"])
print(name["second_name"])
second_name = name["second_name"]
print(second_name[0])
for second in name["second_name"]:
    print(second)
if second_name[0] == "X":
    print(True)