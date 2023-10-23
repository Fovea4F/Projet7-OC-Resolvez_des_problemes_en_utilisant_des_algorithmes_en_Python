from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500


# Ideal Solution Dynamic programmation
def dynamicKnapSac(stockList, maxInvestment):
    # initialize a zeroed matrix
    matrix = [[0.0 for index in range(maxInvestment + 1)] for index in range(len(stockList) + 1)]

    # Fullfill matrix with imported values from file
    for i in range(1, len(stockList) + 1):
        for limitInvest in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= limitInvest:
                matrix[i][limitInvest] = max(stockList[i-1][2]
                                             + matrix[i-1][limitInvest-stockList[i-1][1]],
                                             matrix[i-1][limitInvest])
            else:
                matrix[i][limitInvest] = matrix[i-1][limitInvest]

    limitInvest = maxInvestment
    stockListNumber = len(stockList)
    selectedStockList = []

    while limitInvest >= 0 and stockListNumber >= 0:
        currentProcessedStock = stockList[stockListNumber-1]
        if (matrix[stockListNumber][limitInvest]
            == matrix[stockListNumber-1][limitInvest-currentProcessedStock[1]]
                + currentProcessedStock[2]):

            selectedStockList.append(currentProcessedStock)
            limitInvest -= currentProcessedStock[1]

        stockListNumber -= 1
    profit = matrix[-1][-1]

    return selectedStockList, profit


# --Main--

# get data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)
dataFile = pd.read_csv('./data/list20.csv', sep=';', engine='python')

stockList = []
valuedStockList = []
for row in range(len(dataFile)):
    lineTuple = (dataFile.iloc[row, 0], dataFile.iloc[row, 1], dataFile.iloc[row, 2])
    stockList.append(lineTuple)

# transform percent profit in valued profit in tuple array created
for stock in range(len(stockList)):
    valueStockPerf = stockList[stock][1] * (stockList[stock][2] / 100)
    valuedStockList.append((stockList[stock][0], stockList[stock][1], valueStockPerf))

start = perf_counter_ns()
calculatedActionList, profit = dynamicKnapSac(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
sortedCalculatedActionList = []
for index in range(len(calculatedActionList)):
    sortedCalculatedActionList.append(calculatedActionList.pop())
totalInvestment = 0
for index in range(len(sortedCalculatedActionList)):
    totalInvestment += sortedCalculatedActionList[index][1]


# Results display
# print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
# print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")
print("="*80)
print("===              Liste des actions pour un rendement maximal                 ===")
print("="*80)
print("=== {:<28}{:<28}{:<17}===".format("Nom de l'action", "Acquisition (en €)", "Bénéfices en €"))
print("="*80)
for row in range(len(sortedCalculatedActionList)-1):
    stockName = sortedCalculatedActionList[row][0]
    stockValue = sortedCalculatedActionList[row][1]
    stockProfit = sortedCalculatedActionList[row][2]
    print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €', round(stockProfit, 2), ' €'))
    print(f"==={'-'*74}===")
stockName = sortedCalculatedActionList[row+1][0]
stockValue = sortedCalculatedActionList[row+1][1]
stockProfit = sortedCalculatedActionList[row+1][2]
print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €', round(stockProfit, 2), ' €'))
print("="*80)
print("=== {:<29}{:<6}{:<3}{:<2}{:<2}{:<2}===".format('Bénéfices maximisés attendus : ', round(profit, 2), ' €',
                                                      '| Investissement initial : ', totalInvestment, ' € '))
print("="*80)
print("=== {:<3}{:<19}{:<7}{:<10}{:<34}===".format('', 'Temps de calcul : ', round((end - start)/1e9, 4), ' s',
                                                   ' | Méthode :   \"optimizée\" '))
print("="*80)
