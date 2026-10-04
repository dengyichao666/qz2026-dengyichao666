class UserManager:
    def __init__(self):
        self.users = {}

    # 添加用户
    def add_user(self, user_id, name):
        if user_id in self.users:
            return False, "用户ID已存在"
        self.users[user_id] = name
        return True, "添加成功"

    # 查询用户
    def get_user(self, user_id):
        if user_id in self.users:
            return True, self.users[user_id]
        return False, "用户不存在"

    # 修改用户
    def update_user(self, user_id, new_name):
        if user_id not in self.users:
            return False, "用户不存在"
        self.users[user_id] = new_name
        return True, "修改成功"

    # 删除用户
    def delete_user(self, user_id):
        if user_id not in self.users:
            return False, "用户不存在"
        del self.users[user_id]
        return True, "删除成功"


if __name__ == "__main__":
    um = UserManager()
    # 简单演示
    print(um.add_user(1, "张三"))
    print(um.get_user(1))
    print(um.update_user(1, "张三三"))
    print(um.delete_user(1))
