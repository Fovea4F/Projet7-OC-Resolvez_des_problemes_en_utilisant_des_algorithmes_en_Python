from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500




# brute force: search all solutions compatible with investment limit
# Return :
#   - an array of tuples, listing every selected stock needed for the best profit
#   - the best profit value

def bruteForceKnapSac(stockList, maxInvestment, stockListSelection=[]):
    ''' stockList model : ['stockName', value, valuedProfit]'''
    if stockList:
        listStock1, profit1 = bruteForceKnapSac(stockList[1:], maxInvestment, stockListSelection)
        val = stockList[0]
        if val[1] <= maxInvestment:
            listVal2, profit2 = bruteForceKnapSac(stockList[1:], maxInvestment - val[1], stockListSelection + [val])
            if profit1 < profit2:
                return listVal2, profit2

        return listStock1, profit1
    else:
        reponse_A = stockListSelection
        reponse_B = sum([i[2] for i in stockListSelection])
        return reponse_A, reponse_B


# get data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)

dataFile = pd.read_csv('./data/list20.csv', sep=';', engine='python')

stockList = []
valuedStockList = []
for row in range(len(dataFile)):
    lineTuple = (dataFile.iloc[row, 0], dataFile.iloc[row, 1], dataFile.iloc[row, 2])
    stockList.append(lineTuple)
for stock in range(len(stockList)):
    valueStockResult = stockList[stock][1] * (stockList[stock][2] / 100)
    valuedStockList.append((stockList[stock][0], stockList[stock][1], valueStockResult))


# transform percent profit in valued profit

start = perf_counter_ns()
calculatedActionList, profit = bruteForceKnapSac(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")

print("="*80)
print("===              Liste des actions pour un rendement maximal                 ===")
print("="*80)
print("=== {:<28}{:<28}{:<17}===".format("Nom de l'action", "Acquisition (en €)", "Bénéfices en €"))
print("="*80)
for row in range(len(calculatedActionList)-1):
    stockName = calculatedActionList[row][0]
    stockValue = calculatedActionList[row][1]
    stockProfit = calculatedActionList[row][2]
    print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €', round(stockProfit, 2), ' €'))
    print(f"==={'-'*74}===")
stockName = calculatedActionList[row+1][0]
stockValue = calculatedActionList[row+1][1]
stockProfit = calculatedActionList[row+1][2]
print("=== {:<3}{:<31}{:<3}{:<24}{:<9}{:<3}===".format('', stockName, stockValue, ' €', round(stockProfit, 2), ' €'))
print("="*80)
print("=== {:<29}{:<6}{:<3}{:<2}{:<2}{:<2}===".format('Bénéfices maximisés attendus : ', round(profit, 2), ' €',
                                                      '| Investissement initial : ', maxInvestAmount, ' € '))
print("="*80)
print("=== {:<3}{:<19}{:<7}{:<44}===".format('', 'Temps de calcul : ', round((end - start)/1e9, 4), ' s'))
print("="*80)