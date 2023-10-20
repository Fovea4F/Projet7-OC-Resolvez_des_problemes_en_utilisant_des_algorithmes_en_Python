import time

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
        for limitInvest in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= limitInvest:
                matrice[i][limitInvest] = max(stockList[i-1][2]
                                         + matrice[i-1][limitInvest-stockList[i-1][1]],
                                         matrice[i-1][limitInvest])
            else:
                matrice[i][limitInvest] = matrice[i-1][limitInvest]

    limitInvest = maxInvestment
    stockListNumber = len(stockList)
    selectedStockList = []

    while limitInvest >= 0 and n >= 0:
        currentProcessedStock = stockList[n-1]
        if matrice[n][limitInvest] == matrice[n-1][limitInvest-currentProcessedStock[1]] + currentProcessedStock[2]:
            selectedStockList.append(currentProcessedStock)
            limitInvest -= currentProcessedStock[1]

        n -= 1

    return matrice[-1][-1], selectedStockList


# Nom
# Poids
# Valeur


stockList = [["Action-1", 20, 5], ["Action-2", 30, 10], ["Action-3", 50, 15],
              ["Action-4", 70, 20], ["Action-5", 60, 17], ["Action-6", 80, 25],
              ["Action-7", 22, 7], ["Action-8", 26, 11], ["Action-9", 48, 13],
              ["Action-10", 34, 27], ["Action-11", 42, 17],
              ["Action-12", 110, 9], ["Action-13", 38, 23],
              ["Action-14", 14, 1], ["Action-15", 18, 3], ["Action-16", 8, 8],
              ["Action-17", 4, 12], ["Action-18", 10, 14],
              ["Action-19", 24, 21], ["Action-20", 114, 18]]

ele = [('boule de Bowling', 3, 6),
       ('montre à gousset', 2, 10),
       ("portrait de Tata Janine", 4, 12)]

valuedStockList = []
for stock in range(len(stockList)):
    valueStockResult = stockList[stock][1] * (stockList[stock][2] / 100)
    valuedStockList.append((stockList[stock][0], stockList[stock][1], valueStockResult))

'''start = time.process_time()
print(f"Algo naïf : , {basicKnapSac(500, valuedStockList)}")
end = time.process_time()
print(f"Temps écoulé pour naïf: {end - start}")

start = time.process_time()
print(f"Algo force brute : , {bruteForceKnapSac(500, valuedStockList)}")
end = time.process_time()
print(f"Temps écoulé pour bruteForce: {end - start}")'''

start = time.process_time()
print(f"Algo dynamique : {dynamicKnapSac(500, valuedStockList)}")
end = time.process_time()
print(f"Temps écoulé pour dynamic: {end - start}")
