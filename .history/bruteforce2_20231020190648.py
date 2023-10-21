from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500

'''stockList = [["Action-1", 20, 5], ["Action-2", 30, 10], ["Action-3", 50, 15],
             ["Action-4", 70, 20], ["Action-5", 60, 17], ["Action-6", 80, 25],
             ["Action-7", 22, 7], ["Action-8", 26, 11], ["Action-9", 48, 13],
             ["Action-10", 34, 27], ["Action-11", 42, 17],
             ["Action-12", 110, 9], ["Action-13", 38, 23],
             ["Action-14", 14, 1], ["Action-15", 18, 3], ["Action-16", 8, 8],
             ["Action-17", 4, 12], ["Action-18", 10, 14],
             ["Action-19", 24, 21], ["Action-20", 114, 18]]'''


# brute force: search all solutions compatible with investment limit
def bruteForceKnapSac(stockList, maxInvestment, stockListSelection=[]):
    ''' stockList model : ['stockName', value, valuedProfit]'''
    if stockList:
        listVal1, val1 = bruteForceKnapSac(stockList[1:], maxInvestment, stockListSelection)
        val = stockList[0]
        if val[1] <= maxInvestment:
            listVal2, val2 = bruteForceKnapSac(stockList[1:], maxInvestment - val[1], stockListSelection + [val])
            if val1 < val2:
                return listVal2, val2

        return listVal1, val1
    else:
        reponse_A = stockListSelection
        reponse_B = sum([i[2] for i in stockListSelection])
        return reponse_A, reponse_B


# gest data from .csv file, create tuple array ('actionName', acquisitionValue, percentProfit)
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
'''valuedStockList = []
for stock in range(len(stockList)):
    valueStockResult = stockList[stock][1] * (stockList[stock][2] / 100)
    valuedStockList.append((stockList[stock][0], stockList[stock][1], valueStockResult))'''

start = perf_counter_ns()
calculatedActionList, profit = bruteForceKnapSac(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
print(f"Temps de calcul par approche force brute: {((end - start)/1e9):.4f}s")

print("==========================================================================")
print("===   Liste des actions pour un rendement ma{:<5}{:<20}{:<15}{:<40}".format("Rang", "Date de début", "État", "Nom"))

print("=== {:<5}{:<20}{:<15}{:<40}".format("Rang", "Date de début", "État", "Nom"))
print("="*80)
for _ in enumerate(_tournament_list, start=1):
status = _[1].status
match status:
    case "registered":
        status = "enregistré"
    case "selected":
        status = "sélectionné"
    case "started":
        status = "en cours"
    case "ended":
        status = "terminé"
print("=== {:<5}{:<20}{:<15}{:<40}".format(_[0], _[1].begin_date, status, _[1].name))
"""print(f"=== {_[0]}.{'':<2} {'Nom           : ':<15}{_[1].name}")
print(f"=== {'':<5}{'Lieu          : ':<15}{_[1].location}")
print(f"=== {'':<5}{'Date de début : ':<15}{_[1].begin_date}")
print(f"=== {'':<5}{'Date de fin   : ':<15}{_[1].begin_date}")"""
if not (_[1] == _tournament_list[-1]):
    print("-"*80)