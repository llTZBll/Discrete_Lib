############################### 关系型值判断 ###############################
def check_relations(matrix):
    n = len(matrix)
    properties = {
        "自反": True,
        "反自反": True,
        "对称": True,
        "反对称": True,
        "传递": True
    }

    # 自反性
    for i in range(n):
        if matrix[i][i] != 1:
            properties["自反"] = False
        else:
            properties["反自反"] = False

    # 反自反性
    if properties["自反"] is False:
        for i in range(n):
            if matrix[i][i] != 0:
                properties["反自反"] = False

    # 对称性
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != matrix[j][i]:
                properties["对称"] = False

    # 反对称性
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                properties["反对称"] = False

    # 递性
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] != 1:
                    properties["传递"] = False

    return properties

############################### 闭包计算 ###############################
def reflexive_closure(matrix):
    """计算自反闭包：r(R) = R ∪ I_A"""
    n = len(matrix)
    closure = [row.copy() for row in matrix]
    for i in range(n):
        closure[i][i] = 1  # 确保主对角线全为1
    return closure

def symmetric_closure(matrix):
    """计算对称闭包：s(R) = R ∪ R⁻¹"""
    n = len(matrix)
    closure = [row.copy() for row in matrix]
    for i in range(n):
        for j in range(n):
            if closure[i][j] == 1 and closure[j][i] == 0:
                closure[j][i] = 1  # 添加对称元素
    return closure

def warshall_algorithm(matrix):
    """Warshall算法计算传递闭包：t(R)"""
    n = len(matrix)
    closure = [row.copy() for row in matrix]
    for i in range(n):
        for j in range(n):
            if closure[j][i] == 1:  # 若第j行第i列为1
                for k in range(n):
                    closure[j][k] = closure[j][k] or closure[i][k]  # 逻辑或更新
    return closure

def transitive_closure(matrix):
    return warshall_algorithm(matrix)

############################### 主程序 ###############################
def main():
    n = int(input("请输入集合元素个数n："))
    print("请按行输入关系矩阵（每行输入n个0或1，用空格分隔）：")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 判断关系性质
    properties = check_relations(matrix)
    print("\n关系性质判断结果：")
    for prop, status in properties.items():
        print(f"{prop}: {status}")

    # 计算闭包
    r_closure = reflexive_closure(matrix)
    s_closure = symmetric_closure(matrix)
    t_closure = transitive_closure(matrix)

    # 输出结果
    print("\n闭包计算结果：")
    print("自反闭包 r(R):")
    for row in r_closure:
        print(row)
    print("\n对称闭包 s(R):")
    for row in s_closure:
        print(row)
    print("\n传递闭包 t(R)（Warshall算法）:")
    for row in t_closure:
        print(row)

if __name__ == "__main__":
    main()