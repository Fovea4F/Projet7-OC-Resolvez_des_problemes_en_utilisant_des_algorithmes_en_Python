from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500


# brute force: search all solutions compatible with investment limit
def bruteForceKnapSac(stockList, maxInvestment, stockListSelection=[]):
    ''' stockList model : ['stockName', value, profit]'''
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
start = perf_counter_ns()
calculatedActionList, profit = bruteForceKnapSac(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
print(f"Temps écoulé pour bruteForce: {((end - start)/1e9):.4f}s")