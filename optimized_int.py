'''knapSack algorithm usage, with only integers as weight input'''

from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500
inputFile = './data/list20.csv'


# Ideal Solution Dynamic programmation
def knapSack(stockList, maxInvestment):
    # initialize a zeroed matrix
    matrix = [[0 for index in range(maxInvestment + 1)] for index in range(len(stockList) + 1)]

    # Fulfill matrix with imported values from file
    for i in range(1, len(stockList) + 1):
        for investAmount in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= investAmount:
                matrix[i][investAmount] = max(stockList[i-1][2] + matrix[i-1][investAmount-stockList[i-1][1]],
                                              matrix[i-1][investAmount])
            else:
                matrix[i][investAmount] = matrix[i-1][investAmount]

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
dataFile = pd.read_csv(inputFile, sep=',', engine='python')

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
calculatedActionList, profit = knapSack(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
reOrderedCalculatedActionList = []
for index in range(len(calculatedActionList)):
    reOrderedCalculatedActionList.append(calculatedActionList.pop())
totalInvestment = 0
for index in range(len(reOrderedCalculatedActionList)):
    totalInvestment += reOrderedCalculatedActionList[index][1]


# Results display
# print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
# print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")
print("="*86)
print("==={:>61}{:>19}===".format("Liste des actions pour un rendement maximal", ""))
print("="*86)
print("==={:>17}{:>31}{:>26}{:>6}===".format("Nom de l'action", "Acquisition (en €)", "Bénéfices (en €)", ""))
print("="*86)
for row in range(len(reOrderedCalculatedActionList)-1):
    stockName = reOrderedCalculatedActionList[row][0]
    stockValue = reOrderedCalculatedActionList[row][1]
    stockProfit = reOrderedCalculatedActionList[row][2]
    print("==={:>14}{:>28}{:>2}{:>24}{:>2}{:>10}===".format(stockName, f"{stockValue:.2f}", ' €',
                                                            f"{stockProfit:.2f}", ' €', ''))
    print(f"==={'-'*80}===")
stockName = reOrderedCalculatedActionList[row+1][0]
stockValue = reOrderedCalculatedActionList[row+1][1]
stockProfit = reOrderedCalculatedActionList[row+1][2]
print("==={:>14}{:>28}{:>2}{:>24}{:>2}{:>10}===".format(stockName, f"{stockValue:.2f}", ' €',
                                                        f"{stockProfit:.2f}", ' €', ''))
print("="*86)
print("==={:>31}{:>9}{:>2}{:>27}{:>8}{:>1}{:>1}===".format(' Bénéfices maximisés attendus : ', f"{profit:.2f}", ' €',
                                                           '| Investissement initial : ',
                                                           f"{totalInvestment:.2f}", '€', ''))
print("="*86)
print("==={:>22}{:>11}{:>2}{:>33}{:>12}===".format('Temps de calcul : ', f"{(end - start)/1e9:.4f}", ' s',
                                                   ' | Méthode :   \"optimisée\" ', ''))
print("="*86)
