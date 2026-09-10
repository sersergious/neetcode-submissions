# Time: 50
# Reflection: even fresh after doing the implement the trie problem, this new problem had me look at the solution because i was stumped by the wildcard search. I recognized tht it's a mix of iterative and sort of backtracking DFS search for the wild card, but still.. 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                
            return cur.isEnd
        
        return dfs(0, self.root)
                


