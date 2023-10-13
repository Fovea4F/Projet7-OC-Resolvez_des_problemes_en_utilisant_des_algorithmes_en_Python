class Solution:
    def __init__(self, n: int) -> int;
    
    self.n = step_number
    
    def climbStairs(self):

        match step_number :
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return climbStairs(n-1)

value = Solution.c