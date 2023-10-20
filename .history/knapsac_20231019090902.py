def knapSac_naif(capacity, elements):
    sorted_elements = sorted(elements, key=lambda x: x[2])
    elementsSelection = []
    total_weight = 0

    while sorted_elements:
        element = sorted_elements.pop()
        if element[1] - total_weight <= capacity:
            elementsSelection.append(element)
            total_weight += element[1]

    return sum([i[2] for i in elementsSelection]), elementsSelection


# brute force search all solutions
def bruteForceKnapSac(capacity, elements, elementsSelection=[]):
    if elements:
        val1, listVal1 = bruteForceKnapSac(capacity, elements[1:], elementsSelection)
        val = elements[0]
        if val[1] <= capacity:
            val2, listVal2 = bruteForceKnapSac(capacity - val[1], elements[1:], elementsSelection + [val])
            if val1 < val2:
                return val2, listVal2

        return val1, listVal1
    else:
        return sum([i[2] for i in elementsSelection])


# Ideal Solution Dynamic programmation
def dynamicKnapSac(capacity, elements):
    matrice = [[0 for index in range(capacity + 1) for index in range(elements) + 1]]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacity + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = capacity
    n = len(elements)
    elementsSelection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elementsSelection.append(e)
            w -= e[1]

        n -= 1

