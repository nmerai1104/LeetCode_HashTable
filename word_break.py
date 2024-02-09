class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        # dp[i] represents whether the substring s[:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # An empty string is always a valid segmentation

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
