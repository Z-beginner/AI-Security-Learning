password = input('Enter your password:')
length = len(password)
if length <8:
    print('密码不能小于八位数')
if "word" in password or "pass" in password:
    print("密码中含非法字符")
if length <8 or "word" in password or "pass" in password:
    print('请重新设置密码')