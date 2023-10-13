'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hyphenationIndex = 1
tmpSweepArray = valuesArray # temporary array for combinations loop
newCombinationArray = []
combinationsArray = {}
purchaseThreshold = 52


def arrayMemberSum(array=[]):
    # calculate sum of every leftArrayMember
    totalSum = 0
    for index in range(len(array)):
        totalSum += array[index]
    return totalSum


while len(tmpSweepArray) > 1:
    for newArrayIndex in range(len(valuesArray)):
        hyphenationIndex = 1
        tmpSweepArray = valuesArray[newArrayIndex:len(valuesArray)]
        for index in range(len(tmpSweepArray)):
            leftArray = tmpSweepArray[0:hyphenationIndex]
            leftArraySum = arrayMemberSum(leftArray)
            rightArray = tmpSweepArray[hyphenationIndex:len(tmpSweepArray)]
            for rightIndex in range(len(rightArray)):
                valuesPrice = leftArraySum + rightArray[rightIndex]
                if valuesPrice <= purchaseThreshold {
                    combinationsArray
                }
                print(f"Tableau [gauche/droite]: {leftArray}{rightArray},\
                    somme : {valuesPrice} €")
            hyphenationIndex += 1
