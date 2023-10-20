def investTotalAmount(combinationArray):
    totalSum = 0
    for index in range(len(combinationArray)):
        totalSum += combinationArray[index][0]
        # print(totalSum)
    return totalSum


def roiCalculation(combinationArray):
    roi = 0
    for index in range(len(combinationArray)):
        roi += combinationArray[index][0]*combinationArray[index][1]/100
    return roi

def searchBestInvest(array):
    
    bestInvest = 0
    for index in range(array)



def generateCombinations(actionArray, maxInvest):

    def backtrack(start, current_combination, invest):
        # print(f"start: {start}, current_combination : {current_combination}")
        combination = []
        totalSum = investTotalAmount(current_combination)
        if (0 < totalSum <= invest):
            roiAmount = roiCalculation(current_combination)
            combination.append(list(current_combination))
            combination.append(roiAmount)
            combinations.append(list(combination))  # Add the current combination to the list
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
actionList = [["Action-1", 20, 5], ["Action-2", 30, 10], ["Action-3", 50, 15], ["Action-4", 70, 20], ["Action-5", 60, 17],
              ["Action-6", 80, 25], ["Action-7", 22, 7], ["Action-8", 26, 11], ["Action-9", 48, 13], ["Action-10", 34, 27], ["Action-11"42, 17], [110, 9], [38, 23], [14, 1], [18, 3], [8, 8], [4, 12], [10, 14], [24, 21], [114, 18]]

maxInvest = 500

array = [1, 2, 3, 4]

combinations = generateCombinations(actionList, maxInvest)


for index in range(len(combinations)):
    print(f"Liste combinaisons : {combinations[index]}")

print(f"Nombre de combinaisons : {len(combinations)}")
# valeur = [2, 3, 4]
# print(([2, 3, 6, 7, 9] in combinations))
