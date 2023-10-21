'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hyphenationIndex = 0
tmpSweepArray = valuesArray  # temporary array for combinations loop
newCombinationArray = []
combinationsArray = []
purchaseThreshold = 52


def arrayMemberSum(array=[]):
    # calculate sum of every leftArrayMember
    totalSum = 0
    for index in range(len(array)):
        totalSum += array[index]
    return totalSum


while len(tmpSweepArray) > 1:
    for newArrayIndex in range(len(while len(tmpSweepArray) > 1:
)):
        hyphenationIndex = 0
        tmpSweepArray = valuesArray[newArrayIndex:len(valuesArray)]
        for index in range(len(tmpSweepArray)):
            leftArray = tmpSweepArray[0:hyphenationIndex]
            leftArraySum = arrayMemberSum(leftArray)
            rightArray = tmpSweepArray[hyphenationIndex:len(tmpSweepArray)]
            for rightIndex in range(len(rightArray)):
                newCombinationArray = leftArray
                print(f"Nouvelle combinaison 0: {newCombinationArray}")
                valuesPrice = leftArraySum + rightArray[rightIndex]
                if (valuesPrice <= purchaseThreshold):
                    newCombinationArray.append(valuesArray[len(leftArray) + rightIndex - 1])
                    print(f"Nouvelle combinaison : {newCombinationArray}")
                    combinationsArray.append(newCombinationArray)
                print(f"{combinationsArray}, somme : {valuesPrice} €")
            hyphenationIndex += 1