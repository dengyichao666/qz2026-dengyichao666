一·1.B  2.B 3.B 4.B 5.B 6.B 7.B 8.B 9.B 10.B
二·1. 关系：a 是原始列表；b 是 a 的浅拷贝，它们共享内部子列表的引用；c 是 a 的深拷贝，c 与 a 完全独立。
2. 执行 a[0].append(99) 后，a 变成 [[1, 2, 99], [3, 4]]，b 也变成 [[1, 2, 99], [3, 4]]，c 保持不变，仍为 [[1, 2], [3, 4]]。
3. 原因：浅拷贝只复制最外层，对于b的嵌套不起作用，c是深拷贝，与a完全独立。

第2题：字典与列表的综合应用
答：
1. 找出所有 level 为 "ERROR" 的记录：
   error_logs = [log for log in logs if log["level"] == "ERROR"]

2. 统计每个用户出现的次数：
   user_count = {}
   for log in logs:
       user = log["user"]
       user_count[user] = user_count.get(user, 0) + 1

3. 区别：
   len(logs) 得到的结果是 5，表示这个列表里有几个字典。
   需要for语句遍历所有列表。

第3题：异常处理设计
答：
代码实现：
def safe_divide(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        return num_a / num_b
    except (ValueError, ZeroDivisionError):
        return None

为什么用 try/except 更好：
使用 try/except 更符合 Python 的 EAFP 风格（先尝试执行，遇到错误再处理），代码更简洁。如果用 if 预判，需要写很多代码来检查字符串是否能转为浮点数，并且很难完全覆盖所有异常情况。try/except 能够更优雅地集中处理异常，可读性更高。
