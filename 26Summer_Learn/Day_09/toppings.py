def letter(*toppings):
    for i in toppings:
        print(i)
letter("a", "b", "c")
letter("a", "b", "c", "d")

def letters(*words):
    for i in words:
        print(i)
letters("a", "b", "c", "d")

#加上*    创建一个tuple
#可以传递任意数量形参

def letters2(word, *toppings):
    for i in word:
        print(i)
    for i in toppings:
        print(i)
letters2("a", "b", "c", "d")

#加上**     传递任意数量关键词实参
def letters3(word, **toppings):
    for i in word:
        print(i)
    print(type(toppings))
    for i in toppings.items():
        print(type(i))
    for i in toppings.values():
        print(i)
letters3("a", B="c", D="f")

dic1 = {"a": 1, "b": 2, "c": 3}
for i in dic1.items():
    print(type(i))
#i储存的是一个个(a,b)，即变成了tuple

# 注意：
# *args代表收集任意数量的位置实参
# **kwargs代表收集任意数量的关键字实参