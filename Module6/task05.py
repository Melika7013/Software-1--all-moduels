def remove_odd_numbers(numbers):
    new_list = [num for num in numbers if num % 2 == 0]
    return new_list
original_list = [12, 23, 3, 28, 47, 6, 123, 8]
filtered_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("Filtered list (even numbers only):", filtered_list)
