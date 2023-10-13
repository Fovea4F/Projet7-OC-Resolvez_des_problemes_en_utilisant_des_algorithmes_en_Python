class Solution:
    def __init__(self, n: int) -> int;
    
    self.step_number = n
    
    def climbStairs(self):

        match step_number :
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return climbStairs(step_number-1)

value = Solution(20)
