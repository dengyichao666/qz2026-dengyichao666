from main import UserManager

def test_all():
    um = UserManager()
    # 测试新增
    ok, msg = um.add_user(101, "小明")
    print("新增101：", ok, msg)
    assert ok == True

    # 重复新增
    ok, msg = um.add_user(101, "小明")
    print("重复新增：", ok, msg)
    assert ok == False

    # 查询
    ok, name = um.get_user(101)
    print("查询101：", ok, name)
    assert name == "小明"

    # 修改
    ok, msg = um.update_user(101, "小李")
    print("修改101：", ok, msg)
    assert ok == True

    # 删除
    ok, msg = um.delete_user(101)
    print("删除101：", ok, msg)
    assert ok == True

    # 删除后再查
    ok, msg = um.get_user(101)
    print("删除后查询：", ok, msg)
    assert ok == False

    print("\n✅ 全部测试通过！")

if __name__ == "__main__":
    test_all()
