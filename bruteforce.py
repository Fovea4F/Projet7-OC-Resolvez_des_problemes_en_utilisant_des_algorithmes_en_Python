from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500
inputFile = './data/list4.csv'


# brute force: search all solutions compatible with investment limit
# Return :s
#   - an array of tuple, listing every selected stock needed for the best profit
#   - the best profit value

def knapSack(stockList, maxInvestment, stockListSelection=[]):
    ''' stockList model : ['stockName', value, valuedProfit]'''
    if stockList:
        listStock1, profit1 = knapSack(stockList[1:], maxInvestment, stockListSelection)
        element = stockList[0]
        # can object be inserted in KnapSac ?
        if element[1] <= maxInvestment:
            listVal2, profit2 = knapSack(stockList[1:], maxInvestment - element[1], stockListSelection + [element])
            if profit1 < profit2:
                return listVal2, profit2

        return listStock1, profit1

    else:
        finalProfit = sum([i[2] for i in stockListSelection])
        return stockListSelection, finalProfit


# -------------------------------------------------------------------------------------------------------------
# -- Main --
# -------------------------------------------------------------------------------------------------------------

# get data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)
dataFile = pd.read_csv(inputFile, sep=',', engine='python')

stockList = []
valuedStockList = []
for row in range(len(dataFile)):
    lineTuple = (dataFile.iloc[row, 0], dataFile.iloc[row, 1], dataFile.iloc[row, 2])
    stockList.append(lineTuple)

# transform percent profit in valued profit in tuple array created
for stock in range(len(stockList)):
    valueStockResult = stockList[stock][1] * (stockList[stock][2] / 100)
    valuedStockList.append((stockList[stock][0], stockList[stock][1], valueStockResult))

start = perf_counter_ns()
calculatedActionList, profit = knapSack(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
totalInvestment = 0
for index in range(len(calculatedActionList)):
    totalInvestment += calculatedActionList[index][1]

# Results display
# print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
# print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")
print("="*80)
print("===              Liste des actions pour un rendement maximal                 ===")
print("="*80)
print("=== {:<28}{:<28}{:<17}===".format("Nom de l'action", "Acquisition (en €)", "Bénéfices en €"))
print("="*80)
for row in range(len(calculatedActionList)-1):
    stockName = calculatedActionList[row][0]
    stockValue = calculatedActionList[row][1]
    stockProfit = calculatedActionList[row][2]
    print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €',
                                                           round(stockProfit, 2), ' €'))
    print(f"==={'-'*74}===")
stockName = calculatedActionList[row+1][0]
stockValue = calculatedActionList[row+1][1]
stockProfit = calculatedActionList[row+1][2]
print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €', round(stockProfit, 2), ' €'))
print("="*80)
print("=== {:<29}{:<6}{:<3}{:<2}{:<2}{:<2}===".format('Bénéfices maximisés attendus : ', round(profit, 2), ' €',
                                                      '| Investissement initial : ', totalInvestment, ' € '))
print("="*80)
print("=== {:<3}{:<19}{:<7}{:<10}{:<34}===".format('', 'Temps de calcul : ', round((end - start)/1e9, 4), ' s',
                                                   ' | Méthode : \"force brute\"'))
print("="*80)
