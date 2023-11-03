'''knapSack algorithm usage
   You need to adapt inputFile variable to your environment
'''

from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500
inputFile = './data/dataset2_Python_P7.csv'


# Ideal Solution Dynamic programmation
def knapSack(stockList, maxInvestment):
    # initialize a zeroed matrix
    array = [[0 for index in range(maxInvestment + 1)] for index in range(len(stockList) + 1)]

    # Calculate profit for every weight, when adding an element to array
    for i in range(1, len(stockList) + 1):
        for invest in range(1, maxInvestment + 1):
            if stockList[i-1][1] <= invest:
                array[i][invest] = max(stockList[i-1][2] + array[i-1][invest-stockList[i-1][1]],
                                       array[i-1][invest])
            else:
                array[i][invest] = array[i-1][invest]

    capacityInvest = maxInvestment
    stockListNumber = len(stockList)
    selectedStockList = []

    # build selected stock list from precedent array
    while capacityInvest >= 0 and stockListNumber >= 0:
        currentProcessedStock = stockList[stockListNumber-1]
        if (array[stockListNumber][capacityInvest]
            == array[stockListNumber-1][capacityInvest-currentProcessedStock[1]]
                + currentProcessedStock[2]):

            selectedStockList.append(currentProcessedStock)
            capacityInvest -= currentProcessedStock[1]

        stockListNumber -= 1

    profit = array[-1][-1]
    return selectedStockList, profit


# -----------------------------------------------------------------------------------------------------------
# -- Main --
# -----------------------------------------------------------------------------------------------------------


# get data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)
dataFile = pd.read_csv(inputFile, sep=',', engine='python')
# It is obviously illogical to get shares for free or at a negative price, certainly due to errors, I reject these lines
filter = dataFile['price'] > 0

filteredDataFile = dataFile[filter]
# print(filteredDataFile)
stockList = []
valuedStockList = []
for row in range(len(filteredDataFile)):
    lineTuple = (filteredDataFile.iloc[row, 0], filteredDataFile.iloc[row, 1], filteredDataFile.iloc[row, 2])
    stockList.append(lineTuple)

# transform stock value from decimal to integer, to be compatible to knapSack algorithm
for stock in range(len(stockList)):
    valueStockPerf = stockList[stock][1] * (stockList[stock][2] / 100)
    valueStock = int(stockList[stock][1] * 100)
    valuedStockList.append((stockList[stock][0], valueStock, valueStockPerf))

start = perf_counter_ns()
# The amount of maxInvest is multiplied by 100 to remain consistent with the transformation of the share value
calculatedActionList, profit = knapSack(valuedStockList, maxInvestAmount * 100)
end = perf_counter_ns()

reOrderedCalculatedActionList = []
for index in range(len(calculatedActionList)):
    tmpValue = calculatedActionList.pop()
    # reassign good value to weight
    value = (tmpValue[0], tmpValue[1]/100, tmpValue[2])
    reOrderedCalculatedActionList.append(value)
totalInvestment = 0
for index in range(len(reOrderedCalculatedActionList)):
    totalInvestment += reOrderedCalculatedActionList[index][1]
print((f"longueur liste : {len(reOrderedCalculatedActionList)}"))

# Results display

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
print("==={:>28}{:>7}{:>3}{:>8}{:>24}{:>1}===".format(' Temps de calcul => Total :', f"{(end - start)/1e9:.3f}", 's |',
                                                      f"{(end - start)/(len(valuedStockList))/1e6:.4f}",
                                                      'ms/action | Méthode : "optimisée"', ''))
print("="*86)
