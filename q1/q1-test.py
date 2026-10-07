from main import analyze_log

def test_case():
    """示例1：正常日志文件"""
    result1 = analyze_log("app.jsonl")
    print("总条数：", result1["total"])
    print("按级别统计：", result1["by_level"])
    print("按用户统计：", result1["by_user"])
    print("最后一条错误信息：", result1["last_error"])

    """示例2：文件不存在"""
    result2 = analyze_log("not_exist.jsonl")
    print(\n"文件不存在测试：", result2)

    """示例3：空文件"""
    result3 = analyze_log("empty.jsonl")
    print("\n空文件测试：", result3)

    """示例4：含有非法json行"""
    result4 = analyze_log("bad.jsonl")
    print("\n含错误行测试：")
    print(result4["total"])
    print(result4["by_level"])
    print(result4["last_error"])

if _name_ == "_main_":
    test_case()
