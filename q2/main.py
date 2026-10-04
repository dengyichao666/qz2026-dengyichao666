import json
class UserManager:
    """用户管理器"""
    def __init__(self):
        """初始化"""
        self.users = {}
        self.next_id = 1

    def add_user(self, user_id, name,age):
        """添加用户"""
        user_id =self.next_id
        if user_id in self.users:    
            return False, "用户ID已存在"
        self.users[user_id] = {"id":user_id,"name":name,"age",age}
        self.next_id += 1
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
        self.users[user_id]["age"] = new_age
        return True, "修改成功"

    def remove_user(self, user_id):
        """删除用户"""
        if user_id not in self.users:
            return False, "用户不存在"
        del self.users[user_id]
        return True, "删除成功"
    def list_users(self):
        return list(self.users.values())
    def save_to_json(self,filename):
        save_data = {"users":self.users,"next_id":self.next_id}
        with open(filename,"w",encoding = "utf-8") as f:
            json.dump(save_data,f,ensure_ascii = False)
    def load_from_json(self,filename):
        with open(filename,"r",encoding = "urf-8") as f:
            data = json.load(f)
            self.users = data["users"]
            self.next_id = data["next_id"]
