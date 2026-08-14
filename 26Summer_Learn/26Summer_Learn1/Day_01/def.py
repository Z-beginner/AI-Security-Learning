'''
def hello():
    print('Hello')
hello()
-----------------------------------
def check_prompt(prompt):
    if "hack" in prompt:
        print("danger")
    else:
        print("safe")
check_prompt("hello")
check_prompt("attack me")
check_prompt("hack me")
a = input()
check_prompt(a)

def say_hello(name):
    #print('Hello ' + name)
    print(f'Hello {name}')
name = input('请输入你的名字：')
say_hello(name)
'''
def add(a,b):
    return (a + b)
a = int(input())
b = int(input())
result = add(a,b)
print(result)