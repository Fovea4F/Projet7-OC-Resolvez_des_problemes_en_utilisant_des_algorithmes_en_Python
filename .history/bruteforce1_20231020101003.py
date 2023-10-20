def investTotalAmount(combinationArray):
    # calculate money to stock list shares
    totalSum = 0
    for index in range(len(combinationArray)):
        totalSum += combinationArray[index][1]
    return totalSum


def roiCalculation(combinationArray):
    # calculate Return On Investment amount in a specified combination array
    roi = 0.0
    for index in range(len(combinationArray)):
        roi += combinationArray[index][1]*(1+combinationArray[index][2]/100)
    return roi


def searchBestInvestCombination(array):
    # return list of best investment
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
            combination = list(current_combination)
            combination.append(roiAmount)
            combinationsList.append(list(combination))  # Add the current combination to the list

        # print(combinations)
        for index in range(start, len(actionArray)):
            current_combination.append(actionArray[index])  # Add the current element to the combination
            # Recursively explore combinations without the current elementbacktrack(index + 1, current_combination, maxInvest)  
            # print(i+1)
            current_combination.pop()  # Remove the current element to backtrack

    combinationsList = []
    backtrack(0, [], maxInvest)
    return combinationsList


actionList = [["Action-1", 20, 5], ["Action-2", 30, 10], ["Action-3", 50, 15],
              ["Action-4", 70, 20], ["Action-5", 60, 17], ["Action-6", 80, 25],
              ["Action-7", 22, 7], ["Action-8", 26, 11], ["Action-9", 48, 13],
              ["Action-10", 34, 27], ["Action-11", 42, 17],
              ["Action-12", 110, 9], ["Action-13", 38, 23],
              ["Action-14", 14, 1], ["Action-15", 18, 3], ["Action-16", 8, 8],
              ["Action-17", 4, 12], ["Action-18", 10, 14],
              ["Action-19", 24, 21], ["Action-20", 114, 18]]

# actionList = [["Action-16", 8, 8], ["Action-17", 4, 12]]
maxInvest = 500
bestInvestActionsList = []
bestInvestAmount = 0.0
action = ''

# Create all possible combinations
combinations = generateCombinations(actionList, maxInvest)
print(f"liste de combinaisons possibles : {len(combinations)}")
bestInvestIndex = searchBestInvestCombination(combinations)

bestCombination = combinations[bestInvestIndex][0]

for index in range(len(bestCombination)):
    bestInvestActionsList.append(bestCombination[index][0])

for index in range(len(bestCombination)):
    bestInvestAmount += bestCombination[index][1]

acquiredRoiAmount = roiCalculation(bestCombination)

'''print(f"Un investissement dans la liste d'actions {bestInvestActionsList},\
 permet un gain de {'%.2f' % acquiredRoiAmount} € pour une acquisition\
 de {'%.2f' % bestInvestAmount} €, soit une rentabilité de {'%.2f' % (acquiredRoiAmount/bestInvestAmount*100)}%")'''

print(f"Un investissement dans la liste d'actions {bestInvestActionsList},\
 permet le meilleur gain de {'%.2f' % acquiredRoiAmount} € pour une acquisition\
 de {'%.2f' % bestInvestAmount}€ \n\n ")
