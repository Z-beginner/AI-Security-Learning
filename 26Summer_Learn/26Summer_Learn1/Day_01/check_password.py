def check_password(password):
    length = len(password)
    if length < 8:
        return 'weak'
    else:
        return 'strong'
password = (input())
result = check_password(password)
print(result)