class DSU:
    def __init__(self, n) -> None:
        self.par = list(range(n))
        self.rank = [1] * n
        self.numComponents = n
    
    def find(self, v):
        if v != self.par[v]:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, u, v):
        parU = self.find(u)
        parV = self.find(v)

        if parU == parV:
            return 
        
        self.numComponents -= 1
        if self.rank[parU] > self.rank[parV]:
            self.par[parV] = parU
        else: 
            self.par[parU] = parV
            if self.rank[parU] == self.rank[parV]:
                self.rank[parV] += 1
    
    def getNumComponents(self):
        return self.numComponents

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)

        return dsu.getNumComponents()


