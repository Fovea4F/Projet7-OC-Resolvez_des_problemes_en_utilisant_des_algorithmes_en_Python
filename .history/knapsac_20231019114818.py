def basicKnapSac(capacity, elements):
    sorted_elements = sorted(elements, key=lambda x: x[2])
    elementsSelection = []
    total_weight = 0

    while sorted_elements:
        element = sorted_elements.pop()
        if element[1] + total_weight <= capacity:
            elementsSelection.append(element)
            total_weight += element[1]

    return sum([i[1] for i in elementsSelection]), elementsSelection


# brute force search all solutions
def bruteForceKnapSac(maxInvestment, stockList, stockListSelection=[]):
    if elements:
        val1, listVal1 = bruteForceKnapSac(capacity, elements[1:], elementsSelection)
        val = elements[0]maxInvestment
        if val[1] <= capacity:
            val2, listVal2 = bruteForceKnapSac(capacity - val[1], elements[1:], elementsSelection + [val])
            if val1 < val2:
                return val2, listVal2

        return val1, listVal1
    else:
        return sum([i[2] for i in elementsSelection]), elementsSelection


# Ideal Solution Dynamic programmation
def dynamicKnapSac(capacity, elements):
    matrice = [[0 for index in range(capacity + 1)] for index in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for weight in range(1, capacity + 1):
            if elements[i-1][1] <= weight:
                matrice[i][weight] = max(elements[i-1][2] + matrice[i-1][weight-elements[i-1][1]], matrice[i-1][weight])
            else:
                matrice[i][weight] = matrice[i-1][weight]

    weight = capacity
    n = len(elements)
    elementsSelection = []

    while weight >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][weight] == matrice[n-1][weight-e[1]] + e[2]:
            elementsSelection.append(e)
            weight -= e[1]

        n -= 1

    return matrice[-1][-1], elementsSelection


# Nom
# Poids
# Valeur

ele = [('boule de Bowling', 3, 6),
       ('montre à gousset', 2, 10),
       ("portrait de Tata Janine", 4, 12)]

print('Algo naïf : ', basicKnapSac(5, ele))
print('Algo force brute : ', bruteForceKnapSac(5, ele))
print(f"Algo dynamique : {dynamicKnapSac(5, ele)}")
