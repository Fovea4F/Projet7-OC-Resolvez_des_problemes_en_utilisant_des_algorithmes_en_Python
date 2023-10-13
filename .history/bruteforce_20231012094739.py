class Solution:
    def __init__(self, n: int) -> int;
    
    self.def climbStairs(self):

        match n :
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return climbStairs(n-1)

value = Solution.c