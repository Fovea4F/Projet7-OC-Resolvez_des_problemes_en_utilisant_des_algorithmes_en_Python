'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hyphenationIndex = 1
tmpArray = valuesArray

def arrayMemberSum(array=[]):
    # calculate sum of every leftArrayMember
    totalSum = 0
    for index in range(len(array)):
        totalSum += array[index]
    return totalSum


while len(tmpArray) > 0:
    
    for newArrayIndex in range(len(valuesArray)):
        for index in range(len(valuesArray)):
            leftArray = valuesArray[0:hyphenationIndex]
            leftArraySum = arrayMemberSum(leftArray)
            rightArray = valuesArray[hyphenationIndex:len(valuesArray)]
            for rightIndex in range(len(rightArray)):
                valuesPrice = leftArraySum + rightArray[rightIndex]
                print(f"Tableau [gauche]: {leftArray}, somme : {valuesPrice} €")
            hyphenationIndex += 1
    tmpArray = valuesArray[newArrayIndex:len]
