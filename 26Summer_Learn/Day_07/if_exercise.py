current_users = ["John",
                "Doe",
                "Mary",
                "Will",
                "Hanna"]
lower_current_users = [user.lower() for user in current_users]
new_users = ["JOHN",
            "Doe",
            "Harry",
            "Lily",
            "Lisa"]
lower_new_users = [user.lower() for user in new_users]
for new_user in lower_new_users:
    if new_user in lower_current_users:
        print("已被使用,请重新输入")
    else:
        print("未被使用")