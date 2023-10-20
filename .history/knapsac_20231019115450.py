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
    if stockList:
        val1, listVal1 = bruteForceKnapSac(maxInvestment, stockList[1:], stockListSelection)
        val = stockList[0]
        if val[1] <= maxInvestment:
            val2, listVal2 = bruteForceKnapSac(maxInvestment - val[1], stockList[1:], stockListSelection + [val])
            if val1 < val2:
                return val2, listVal2

        return val1, listVal1
    else:
        return sum([i[2] for i in stockListSelection]), stockListSelection


# Ideal Solution Dynamic programmation
def dynamicKnapSac(maxInvestment, stockList):
    matrice = [[0 for index in range(maxInvestment + 1)] for index in range(len(stockList) + 1)]

    for i in range(1, len(stockList) + 1):
        for weight in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= weight:
                matrice[i][weight] = max(stockList[i-1][2]
                                         + matrice[i-1][weight-stockList[i-1][1]],
                                         matrice[i-1][weight])
            else:
                matrice[i][weight] = matrice[i-1][weight]

    weight = maxInvestment
    n = len(stockList)
    selectedStockList = []

    while weight >= 0 and n >= 0:
        currentTreatedStock = stockList[n-1]
        if matrice[n][weight] == matrice[n-1][weight-currentStock[1]] + e[2]:
            selectedStockList.append(currentStock)
            weight -= currentStock[1]

        n -= 1

    return matrice[-1][-1], selectedStockList


# Nom
# Poids
# Valeur

ele = [('boule de Bowling', 3, 6),
       ('montre à gousset', 2, 10),
       ("portrait de Tata Janine", 4, 12)]

print('Algo naïf : ', basicKnapSac(5, ele))
print('Algo force brute : ', bruteForceKnapSac(5, ele))
print(f"Algo dynamique : {dynamicKnapSac(5, ele)}")
