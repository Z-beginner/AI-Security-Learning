class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_attempt = 0
    def login(self):
        self.login_attempt += 1
        return self.login_attempt
z = UserLogin("Z", "password")
z.login()
z.login()
z.login()
z.login()
z.login()
z.login()
print(z.login())