def input_boolean(prompt):
    """辅助函数：获取布尔值输入"""
    while True:
        value = input(prompt).strip().lower()
        if value in {'true', 't', '1', '是', '真'}:
            return True
        elif value in {'false', 'f', '0', '否', '假'}:
            return False
        print("输入无效，请输入 True/False、T/F、1/0 等表示真假的值。")


def logical_and(p, q):
    """合取运算 (P ∧ Q)"""
    return p and q

def logical_or(p, q):
    """析取运算 (P ∨ Q)"""
    return p or q

def logical_implies(p, q):
    """条件运算 (P → Q)"""
    return not p or q

def logical_iff(p, q):
    """双条件运算 (P ↔ Q)"""
    return p == q

def print_truth_table(formula_str):
    """生成并打印命题公式的真值表"""
    # 提取命题变量
    variables = sorted({char for char in formula_str if char.isalpha()})
    n = len(variables)

    # 打印表头
    header = " | ".join(variables) + " | " + formula_str
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    # 生成所有可能的真值组合
    for i in range(2 ** n):
        values = [(i >> j) & 1 for j in reversed(range(n))]
        var_dict = {var: bool(val) for var, val in zip(variables, values)}

        # 替换变量为布尔值并计算表达式
        expr = formula_str
        for var, val in var_dict.items():
            expr = expr.replace(var, 'True' if val else 'False')

        # 替换逻辑运算符为Python等价形式
        expr = expr.replace('∧', 'and')
        expr = expr.replace('∨', 'or')
        expr = expr.replace('→', 'implies')  # 注意：这里需要自定义函数替换
        expr = expr.replace('↔', 'iff')  # 注意：这里需要自定义函数替换
        expr = expr.replace('¬', 'not ')  # 注意空格

        # 为安全起见，使用受限的命名空间进行求值
        safe_dict = {
            'True': True,
            'False': False,
            'and': lambda x, y: x and y,
            'or': lambda x, y: x or y,
            'not': lambda x: not x,
            'implies': lambda x, y: not x or y,
            'iff': lambda x, y: x == y
        }

        try:
            result = eval(expr, {"__builtins__": None}, safe_dict)
        except Exception as e:
            result = f"Error: {e}"

        # 打印当前行
        row = " | ".join(["T" if v else "F" for v in values])
        row += " | " + ("T" if result else "F" if isinstance(result, bool) else str(result))
        print(row)

    print("-" * len(header))

def main():
    """主函数：程序入口点"""
    while True:
        print("\n命题逻辑运算与真值表生成器")
        print("=" * 30)
        print("1. 计算两个命题的逻辑运算")
        print("2. 生成命题公式的真值表")
        print("q. 退出程序")
        choice = input("请选择操作 (1/2/q): ").strip().lower()

        if choice == '1':
            # 输入两个命题的真值
            p = input_boolean("请输入命题 P 的真值 (True/False): ")
            q = input_boolean("请输入命题 Q 的真值 (True/False): ")

            # 计算并输出结果
            print(f"\nP = {p}, Q = {q}")
            print(f"合取 (P ∧ Q): {logical_and(p, q)}")
            print(f"析取 (P ∨ Q): {logical_or(p, q)}")
            print(f"条件 (P → Q): {logical_implies(p, q)}")
            print(f"双条件 (P ↔ Q): {logical_iff(p, q)}")

        elif choice == '2':
            # 输入命题公式
            formula = input("请输入命题公式 (使用 P, Q, R 等变量，逻辑符号: ∧, ∨, ¬, →, ↔): ").strip()
            print_truth_table(formula)

        elif choice == 'q':
            print("程序已退出。")
            break

        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()