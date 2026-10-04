from main import UserManager

if __name__ == "__main__":
    um = UserManager()
    um.add_user("张三",18)
    um.add_user("李四",20)
    print(um.get_user(1))
    print(um.get_use(99))
    print(um.update_age(1,99))
    print(um.remove_user(2))
    print(um.remove_user(2))
    print(um.list_users())
    um.save_to_json("user.json")
    um2 = UserManager()
    um2.load_from_json("users.json")
    print(um2.list_users())
