'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hyphenationIndex = 1


def arrayMemberSum(array=[]):
    # calculate sum of every leftArrayMember
        self.array = array
        sum = 0
        for index in range(len(array)):
            sum += array[index]


for index in range(len(valuesArray)):
    leftArray = valuesArray[0:hyphenationIndex]
    rightArray = valuesArray[hyphenationIndex:len(valuesArray)]
    print(f"Tableau [gauche][droit] : {leftArray}{rightArray}. Somme tableau gauche : {arrayMemberSum(leftArray)}")
    hyphenationIndex += 1
