apples = {
    "clore": "red",
    "size": "small"
}
print(apples)

#add
apples["nums"] = "more"
print(apples)

#change
apples["nums"] = "little"
print(apples)

#remove
del apples["nums"]
print(apples)

#get
apple1 = apples.get("smell", "No Smell")
print(apple1)
apple2 = apples.get("clore", "No Clore")
print(apple2)

#items
for key, value in apples.items():
    print(key, value)

#keys and values
#title lower upper
for key in apples.keys():
    print(key.title())
for value in apples.values():
    print(value.upper())

#sorted
new_apples = sorted(apples.keys())
print(new_apples)
new_apples.reverse()
print(new_apples)