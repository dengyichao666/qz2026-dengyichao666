from main import analyze_log

def test_case():
    """示例1：正常日志文件"""
    res1 = analyze_log("app.jsonl")
    print("总条数：", res1["total"])
    print("按级别统计：", res1["by_level"])
    print("按用户统计：", res1["by_user"])
    print("最后一条错误信息：", res1["last_error"])

    """示例2：文件不存在"""
    res2 = analyze_log("not_exist.jsonl")
    print("文件不存在测试：", res2)
