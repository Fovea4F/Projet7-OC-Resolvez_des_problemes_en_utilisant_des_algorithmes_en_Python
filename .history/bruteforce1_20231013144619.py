def generate_combinations(arr):
    def backtrack(start, current_combination):
        combinations.append(list(current_combination))  # Add the current combination to the list

        for i in range(start, len(arr)):
            current_combination.append(arr[i])  # Add the current element to the combination
            backtrack(i + 1, current_combination)  # Recursively explore combinations without the current element
            current_combination.pop()  # Remove the current element to backtrack

    combinations = []
    backtrack(0, [])
    return combinations

# Example usage:
array = [1, 2, 3]
combinations = generate_combinations(array)
print(combinations)
print(len(combinations))
present = valeur in (cobbinations)
