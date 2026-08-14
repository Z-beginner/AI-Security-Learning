username = input('请输入用户名:')
password = input('请输入密码:')
length = len(password)
if length >= 8 and username == 'admin' and not "123" in password:
    print('登陆成功')
else:
    print('登陆失败')