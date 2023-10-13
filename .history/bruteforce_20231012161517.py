'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indiceHyphenation = 1



for index in range(len(valuesArray)) :
    indiceHyphenation += 1
    leftArray = valuesArray[0:indiceHyphenation]
    rightArray = valuesArray[indiceHyphenation:len(valuesArray)]
    print(f"Tableau [gauche][droit] : {leftArray}{rightArray}")
    