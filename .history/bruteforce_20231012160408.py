'''Analyse par brute force
Calculer toutes les combinaisons possibles,
de somme de membres d'un tableau,
chaque membre utilisé au maximum une fois'''

valuesArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indiceHypenation = 0

leftArray = valuesArray[0:indiceCesure]
rightArray = valuesArray[0:indiceCesure+1:len(valuesArray)]

