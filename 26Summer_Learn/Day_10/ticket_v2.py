from random import choice
total = (1,2,3,4,5,6,7,8,9,10,
         "A","B","C","D","E")
win = True
num = 0
results = set()
while win:
    num += 1
    for i in range(5):
        result = choice(total)
        results.add(type(result))
    if len(results) == 1:
        win = False
        print(num)
    else:
        results = set()