class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visit = set()

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)

