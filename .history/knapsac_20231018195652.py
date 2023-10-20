def knapsac_naif(capacity, elements):
    sorted_elements = sorted(elements, key=lambda x: x[2])
    elements_selection = []
    weigth = 0
    
    while sorted_element:
        