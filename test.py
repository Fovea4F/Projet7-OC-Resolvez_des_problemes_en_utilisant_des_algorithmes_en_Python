from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500


# Ideal Solution Dynamic programmation
def dynamicKnapSac(stockList, maxInvestment):
    # initialize a zeroed matrix
    matrix = [[0 for index in range(maxInvestment + 1)] for index in range(len(stockList) + 1)]

    # Fulfill matrix with imported values from file
    for i in range(1, len(stockList) + 1):
        for limitInvest in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= limitInvest:
                matrix[i][limitInvest] = max(stockList[i-1][2] + matrix[i-1][limitInvest-stockList[i-1][1]],
                                             matrix[i-1][limitInvest])
            else:
                matrix[i][limitInvest] = matrix[i-1][limitInvest]

    capacityInvest = maxInvestment
    stockListNumber = len(stockList)
    selectedStockList = []

    while capacityInvest >= 0 and stockListNumber >= 0:
        currentProcessedStock = stockList[stockListNumber-1]
        if (matrix[stockListNumber][capacityInvest]
            == matrix[stockListNumber-1][capacityInvest-currentProcessedStock[1]]
                + currentProcessedStock[2]):

            selectedStockList.append(currentProcessedStock)
            capacityInvest -= currentProcessedStock[1]

        stockListNumber -= 1
    profit = matrix[-1][-1]

    return selectedStockList, profit


# --Main--

# get data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)
dataFile = pd.read_csv('./data/list20.csv', sep=',', engine='python')
# It is obviously illogical to get shares for free or at a negative price, certainly due to errors, I reject these lines
filter = dataFile['price'] > 0

filteredDataFile = dataFile[filter]
# print(filteredDataFile)
stockList = []
valuedStockList = []
for row in range(len(filteredDataFile)):
    lineTuple = (filteredDataFile.iloc[row, 0], filteredDataFile.iloc[row, 1], filteredDataFile.iloc[row, 2])
    stockList.append(lineTuple)

# transform stock value from decimal to integer, to be compatible to knapsack algorithm
for stock in range(len(stockList)):
    valueStockPerf = stockList[stock][1] * (stockList[stock][2] / 100)
    valueStock = int(stockList[stock][1] * 100)
    valuedStockList.append((stockList[stock][0], valueStock, valueStockPerf))
start = perf_counter_ns()
# maxinvestAmount is mutiplied by 100 to stay coherent with sotock Price transformation
calculatedActionList, profit = dynamicKnapSac(valuedStockList, maxInvestAmount*100)
end = perf_counter_ns()
reversedCalculatedActionList = []
for index in range(len(calculatedActionList)):
    tmpValue = calculatedActionList.pop()
    value = (tmpValue[0], tmpValue[1]/100, tmpValue[2])
    reversedCalculatedActionList.append(value)
totalInvestment = 0
for index in range(len(reversedCalculatedActionList)):
    totalInvestment += reversedCalculatedActionList[index][1]
print((f"longueur liste : {len(reversedCalculatedActionList)}"))

# Results display
# print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
# print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")
print("="*86)
print("==={:>61}{:>19}===".format("Liste des actions pour un rendement maximal", ""))
print("="*86)
print("==={:>17}{:>31}{:>26}{:>6}===".format("Nom de l'action", "Acquisition (en €)", "Bénéfices (en €)", ""))
print("="*86)
for row in range(len(reversedCalculatedActionList)-1):
    stockName = reversedCalculatedActionList[row][0]
    stockValue = reversedCalculatedActionList[row][1]
    stockProfit = reversedCalculatedActionList[row][2]
    print("==={:>14}{:>28}{:>2}{:>24}{:>2}{:>10}===".format(stockName, f"{stockValue:.2f}", ' €',
                                                            f"{stockProfit:.2f}", ' €', ''))
    print(f"==={'-'*80}===")
stockName = reversedCalculatedActionList[row+1][0]
stockValue = reversedCalculatedActionList[row+1][1]
stockProfit = reversedCalculatedActionList[row+1][2]
print("==={:>14}{:>28}{:>2}{:>24}{:>2}{:>10}===".format(stockName, f"{stockValue:.2f}", ' €',
                                                        f"{stockProfit:.2f}", ' €', ''))
print("="*86)
print("==={:>31}{:>9}{:>2}{:>27}{:>8}{:>1}{:>1}===".format(' Bénéfices maximisés attendus : ', f"{profit:.2f}", ' €',
                                                           '| Investissement initial : ',
                                                           f"{totalInvestment:.2f}", '€', ''))
print("="*86)
print("==={:>28}{:>7}{:>3}{:>8}{:>24}{:>1}===".format(' Temps de calcul => Total :', f"{(end - start)/1e9:.2f}", 's |',
                                                      f"{(end - start)/(len(valuedStockList))/1e6:.4f}",
                                                      'ms/action | Méthode : "optimisée"', ''))
print("="*86)
