def investTotalAmount(combinationArray):
    totalSum = 0
    for index in range(len(combinationArray)):
        totalSum += combinationArray[index][1]
        # print(totalSum)
    return totalSum


def roiCalculation(combinationArray):
    roi = 0
    for index in range(len(combinationArray)):
        roi += combinationArray[index][1]*combinationArray[index][2]/100
    return roi


def searchBestInvest(array):

    bestInvest = 0
    bestInvestIndex = 0
    for index in range(len(array)):
        if array[index][1] > bestInvest:
            bestInvest = array[index][1]
            bestInvestIndex = index
    return bestInvestIndex


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


actionList = [["Action-1", 20, 5], ["Action-2", 30, 10], ["Action-3", 50, 15], ["Action-4", 70, 20], ["Action-5", 60, 17],
              ["Action-6", 80, 25], ["Action-7", 22, 7], ["Action-8", 26, 11], ["Action-9", 48, 13], ["Action-10", 34, 27],
              ["Action-11", 42, 17], ["Action-12", 110, 9], ["Action-13", 38, 23], ["Action-14", 14, 1], ["Action-15", 18, 3],
              ["Action-16", 8, 8], ["Action-17", 4, 12], ["Action-18", 10, 14], ["Action-19", 24, 21], ["Action-20", 114, 18]]

maxInvest = 500
bestInvestActionsList = []
bestInvestAmount = 0.0

combinations = generateCombinations(actionList, maxInvest)
bestInvestIndex = searchBestInvest(combinations)
bestCombination = combinations[bestInvestIndex]
for index in range(len(bestCombination[0])):
    print(f)
    bestInvestActionsList.append(combinations[bestInvestIndex][index][0])
for index in range(len(combinations[bestInvestIndex][0])):
    bestInvestAmount += combinations[bestInvestIndex][index][1]
acquiredAmount = combinations[bestInvestIndex][1]

print(f"Afin de maximiser les profits, vous devers investir dans la \
    combinaison suivante : {bestInvestActionsList}, pour une acquisition \
    de {bestInvestAmount} €, afin d'acquérir la somme de {acquiredAmount} €")
