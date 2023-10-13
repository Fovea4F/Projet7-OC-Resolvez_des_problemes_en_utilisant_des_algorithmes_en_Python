class Solution:
    def __init__(self, n: int) -> int:

        self.step_number = n

    def climbStairs(step_number):

        match step_number:
            case 1 :
                return 1
            case 2 :
                return 2
            case _ :
                return Solution.climbStairs(step_number-1)

value = 20
solution = Solution(value)
print(f"Nombre de cas pour {value} : {solution}")

