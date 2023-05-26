def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# Get input from the user
input_list = input("Enter a list of numbers (separated by spaces): ").split()
input_list = [int(num) for num in input_list]

# Call the function
sorted_list = selection_sort(input_list)

# Print the result
print("Sorted List:", sorted_list)
