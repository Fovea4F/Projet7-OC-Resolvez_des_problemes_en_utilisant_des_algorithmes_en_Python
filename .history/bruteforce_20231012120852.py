class Solution:
    def __init__(self, n: int) -> int:

        self.step_number = n

    def climbStairs(step_number):

        if (step_number == 0):
            return 0
        case 1:
                return 1
            case 2:
                return 2
            case _:
                return Solution.climbStairs(step_number-2) + Solution.climbStairs(step_number-1)


value = 40
solution = Solution.climbStairs(value)
print(f"Nombre de cas pour {value} : {solution}")

