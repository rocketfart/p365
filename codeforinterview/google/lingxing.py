def minimumTotal( triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    m = len(triangle)
    top = m / 2

    dp = triangle[top][:]

    for i in range(top - 1, -1, -1):
        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]+triangle[-(i+1)][j]

    return dp[0],dp[1],dp[2]

triangle=[
     [1],
    [1,4],
   [1,5,7],
  [1,1,8,3],
   [1,5,7],
    [20,4],
     [1]
]

print minimumTotal(triangle)


def dfs(s):
    if not s or s in wordDict:
        return True
    for i in range(len(s) + 1):
        if s[:i] in wordDict and dfs(s[i:]):
            return True
    return False


class TrieNode():
    def __init__(self):
        self.dict = {}
        self.isword = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for c in word:
            root = root.dict.setdefault(c, TrieNode())
        root.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for c in word:
            root = root.dict.get(c, None)
            if not root: return False
        return root.isword