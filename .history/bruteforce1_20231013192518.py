def investTotalAmount(combinationArray):
    totalSum = 0
    for index in range(len(combinationArray)):
        totalSum += combinationArray[index][0]
        # print(totalSum)
    return totalSum


def roiCalculation(combinationArray):
    roi = 0
    for index in range(len(combinationArray)):
        roi += combinationArray[index][0]+combinationArray[index][1]
    return roi

def generateCombinations(actionArray, maxInvest):

    def backtrack(start, current_combination, invest):
        # print(f"start: {start}, current_combination : {current_combination}")
        combination = []
        totalSum = investTotalAmount(current_combination)
        roiAmount = roiCalculation(current_combination)
        combination.append(list(current_combination))
        combination.append(roiAmount)
        # if (0 < totalSum <= invest):
            combinations.append(list(current_combination))  # Add the current combination to the list
        # print(combinations)

        for i in range(start, len(actionArray)):
            current_combination.append(actionArray[i])  # Add the current element to the combination
            backtrack(i + 1, current_combination, maxInvest)  # Recursively explore combinations without the current element
            # print(i+1)
            current_combination.pop()  # Remove the current element to backtrack

    combinations = []
    backtrack(0, [], maxInvest)
    return combinations


# Example usage:
actionList = [[20, 5], [30, 10], [50, 15], [70, 20], [60, 17], [80, 25], [22, 7], [26, 11], [48, 13], [34, 27], [42, 17], [110, 9], [38, 23], [14, 1], [18, 3], [8, 8], [4, 12], [10, 14], [24, 21], [114, 18]]

maxInvest = 500

array = [1, 2, 3, 4]

combinations = generateCombinations(actionList, maxInvest)


for index in range(len(combinations)):
    print(f"Liste combinaisons : {combinations[index]}")

print(f"Nombre de combinaisons : {len(combinations)}")
# valeur = [2, 3, 4]
# print(([2, 3, 6, 7, 9] in combinations))
