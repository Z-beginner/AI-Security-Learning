words = ["a","b","c","d","e","f","g"]
print(words[ :4])
print(words[-3:])
for word in words[-2:]:
    print(word)

same_love = ["pizza","cake"]
my_love = same_love[:]
friend_love = same_love[:]
my_love.append("ice cream")
friend_love.append("hamberger")
for love in my_love:
    print(love)
for love in friend_love:
    print(love)

#切片