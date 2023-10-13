class Solution:
    def __init__(self, n: int) -> int;
    def climbStairs(self):

000000        match n :
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return climbStairs(n-1)

value = Solution.c