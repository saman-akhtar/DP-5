class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        if m == 0 or  n== 0:
            return 0
        #using 1 d
         #TC O(mn)
        # SC O(n)
        if n > m:
            return self.uniquePaths(n, m)
        dp = [1]* n
        # starting from  1 i.e m -2 elemnt as dp[m ] already has 1
        for i in range(m-2, -1,-1):
            right = 0
            for j in range(n-1, -1,-1):
                dp[j] = dp[j] + right
                right = dp[j] 
        return dp[0]
        #using 2d
         #TC O(mn)
        # SC O(mn)
        # dp = [[0] * (n + 1) for i in range(m + 1) ]
        # for i in range(m-1, -1,-1):
        #      for j in range(n-1, -1,-1):
        #             print(i,j)
        #             if  i == m -1 or j == n -1:
        #                 dp[i][j] =1
        #                 continue
        #             dp[i][j] = dp[i + 1][j]+ dp[i][j +1]
        # return dp [0][0]
