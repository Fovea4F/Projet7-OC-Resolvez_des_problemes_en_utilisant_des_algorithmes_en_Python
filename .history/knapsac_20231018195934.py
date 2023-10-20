def knapsac_naif(capacity, elements):
    sorted_elements = sorted(elements, key=lambda x: x[2])
    elements_selection = []
    total_weight = 0

    while sorted_element:
        element = sorted_elements.pop()
        if element[1] - total_weight <= capacity:
            elements_selection.append(element)
            to