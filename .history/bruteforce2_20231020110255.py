from time import perf_counter_ns
import pandas as pd

maxInvestAmount = 500



start = perf_counter_ns()
calculatedActionList, profit = bruteForceKnapSac(valuedStockList, maxInvestAmount)
end = perf_counter_ns()
print(f"Liste optimisée d'investissement : {calculatedActionList}, bénéfice réalisé attendu : {profit:.2f}€")
print(f"Temps écoulé pour bruteForce: {((end - start)/1e9):.4f}s")