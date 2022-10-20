class Solution:
    def solve(self, graph):
        ans = 0
        n = len(graph)
        table = [-1] * n
        def dfs(u):
            if table[u] != -1:
                return table[u]
            p_len = 0
            for v in graph[u]:
                p_len = max(p_len, 1 + dfs(v))
            table[u] = p_len
            return p_len
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans
ob = Solution()
graph = [
    [1, 2],
    [3, 4],
    [],
    [4],
    [2],
    ]
print(ob.solve(graph))
