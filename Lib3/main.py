import numpy as np

def matrix_power(matrix, m):
    """计算矩阵的m次幂"""
    result = np.eye(len(matrix), dtype=int)
    for _ in range(m):
        result = np.dot(result, matrix)
    return result

def main():
    # 获取图的类型
    graph_type = input("请输入图的类型（1:有向图, 2:无向图）：")
    while graph_type not in ['1', '2']:
        graph_type = input("输入无效，请重新输入图的类型（1:有向图, 2:无向图）：")

    # 获取节点数
    n = int(input("请输入图的节点数："))
    while n <= 0:
        n = int(input("节点数必须为正整数，请重新输入："))

    # 获取邻接矩阵
    print(f"请输入{n}x{n}的邻接矩阵（每行元素用空格分隔，共{n}行）：")
    adj_matrix = []
    for _ in range(n):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != n:
                    print(f"每行应包含{n}个元素，请重新输入该行：")
                    continue
                adj_matrix.append(row)
                break
            except ValueError:
                print("输入无效，请输入整数：")

    adj_matrix = np.array(adj_matrix)

    # 无向图的邻接矩阵是对称的
    if graph_type == '2':
        adj_matrix = adj_matrix | adj_matrix.T  # 确保对称性

    # 获取路径长度m
    m = int(input("请输入路径长度m："))
    while m <= 0:
        m = int(input("路径长度必须为正整数，请重新输入："))

    # 计算邻接矩阵的m次幂
    result_matrix = matrix_power(adj_matrix, m)

    # 输出结果
    print(f"\n邻接矩阵的{m}次幂为：")
    for row in result_matrix:
        print(' '.join(map(str, row)))

    print("\n两节点间长度为{}的路径数目：".format(m))
    print("起点\\终点", end='')
    for j in range(n):
        print(f"{j + 1:6d}", end='')
    print()
    print("-" * (7 * (n + 1)))
    for i in range(n):
        print(f"{i + 1:6d}|", end='')
        for j in range(n):
            print(f"{result_matrix[i][j]:6d}", end='')
        print()

if __name__ == "__main__":
    main()