from random import choice
total = (1,2,3,4,5,6,7,8,9,10,
         "A","B","C","D","E")
win = True
num = 0
results = []
while win:
    num += 1
    for i in range(5):
        result = choice(total)
        results.append(result)
    print(results)
    type1 = type(results[0])
    type2 = type(results[1])
    type3 = type(results[2])
    type4 = type(results[3])
    if type1==type2==type3==type4:
        win = False
        print(num)
    else:
        results = []