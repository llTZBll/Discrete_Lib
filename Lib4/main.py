class DisjointSet:
    """并查集类，用于检测无向图中的环"""
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parent[y_root] = x_root
        return True


def kruskal(adj_matrix):
    n = len(adj_matrix)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))

    edges.sort(key=lambda x: x[2])

    mst = []
    disjoint_set = DisjointSet(n)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.union(u, v):
            mst.append(edge)
            if len(mst) == n - 1:
                break

    return mst


def main():
    print("请输入图的邻接矩阵（用空格分隔每行的元素，行之间用回车分隔）：")
    print("例如：")
    print("0 2 0")
    print("2 0 3")
    print("0 3 0")

    matrix = []
    while True:
        line = input().strip()
        if not line:
            break
        row = list(map(int, line.split()))
        matrix.append(row)

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("错误：输入的矩阵不是方阵！")
            return

    mst = kruskal(matrix)

    print("\n最小生成树的边集：")
    total_weight = 0
    for edge in mst:
        u, v, weight = edge
        print(f"边: {u} -- {v}, 权重: {weight}")
        total_weight += weight

    print(f"\n最小生成树的总权重: {total_weight}")

if __name__ == "__main__":
    main()