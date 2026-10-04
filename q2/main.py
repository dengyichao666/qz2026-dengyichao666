import json
class UserManager:
    """用户管理器"""
    def __init__(self):
        """初始化"""
        self.users = {}

    def add_user(self, user_id, name,age):
        """添加用户"""
        if user_id in self.users:
            return False, "用户ID已存在"
        self.users[user_id] = name
        return True, "添加成功"

    def get_user(self, user_id):
        """查询用户"""
        if user_id in self.users:
            return True, self.users[user_id]
        return False, "用户不存在"

    def update_user(self, user_id, new_name):
        """修改用户"""
        if user_id not in self.users:
            return False, "用户不存在"
        self.users[user_id] = new_name
        return True, "修改成功"

    def delete_user(self, user_id):
        """删除用户"""
        if user_id not in self.users:
            return False, "用户不存在"
        del self.users[user_id]
        return True, "删除成功"


if __name__ == "__main__":
    um = UserManager()
    # 创建类
    print(um.add_user(1, "张三"))
    print(um.get_user(1))
    print(um.update_user(1, "张三三"))
    print(um.delete_user(1))
