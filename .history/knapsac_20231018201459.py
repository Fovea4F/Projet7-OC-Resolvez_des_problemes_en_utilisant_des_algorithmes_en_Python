def knapsac_naif(capacity, elements):
    sorted_elements = sorted(elements, key=lambda x: x[2])
    elements_selection = []
    total_weight = 0

    while sorted_elements:
        element = sorted_elements.pop()
        if element[1] - total_weight <= capacity:
            elements_selection.append(element)
            total_weight += element[1]

    return sum([i[2] for i in elements_selection]), elements_selection


# brute force search all solutions

def bruteForceKnapsac():
    