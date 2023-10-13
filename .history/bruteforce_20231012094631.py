class Solution:
    
    def climbStairs(self, n: int) -> int;

        match n :
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return climbStairs(n-1)

value = Solution.c