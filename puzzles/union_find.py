class UF:
    def __init__(self, n) -> None:
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            # path compression
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return

        # small tree connect below large tree
        if self.size[root_u] > self.size[root_v]:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        else:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        self.count -= 1
