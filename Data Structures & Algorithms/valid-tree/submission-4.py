class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1 for _ in range(n + 1)]
        self.numComponents = n

    def find(self, v):
        if v != self.par[v]:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, u, v):
        parU = self.find(u)
        parV = self.find(v)

        if parU == parV:
            return False 

        self.numComponents -= 1
        if self.rank[parU] > self.rank[parV]:
            self.par[parV] = parU
        else:
            self.par[parU] = parV
            if self.rank[parU] == self.rank[parV]:
                self.rank[parU] += 1
        
        return True
    
    def getNumComponents(self):
        return self.numComponents

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return dsu.getNumComponents() == 1