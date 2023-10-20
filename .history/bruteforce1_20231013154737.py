def generate_combinations(arr):
    def backtrack(start, current_combination):
        # print(f"start: {start}, current_combination : {current_combination}")
        combinations.append(list(current_combination))  # Add the current combination to the list

        for i in range(start, len(arr)):
            current_combination.append(arr[i])  # Add the current element to the combination
            backtrack(i + 1, current_combination)  # Recursively explore combinations without the current element
            # print(i+1)
            current_combination.pop()  # Remove the current element to backtrack

    combinations = []
    backtrack(0, [])
    return combinations


# Example usage:
arrayIn = []
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for index in range(5):
    for indexInside in range(len(array)):
        arrayIn.append(array[indexInside]+20 index)
print(arrayIn)
# combinations = generate_combinations(arrayIn)

# print(combinations)
# print(f"Nombre de combinaisons : {len(combinations)}")
# valeur = [2, 3, 4]
# print(([2, 3, 6, 7, 9] in combinations))
