def get_sublist(list, start_index, end_index):
    sublist = list[start_index:end_index+1:2]
    return sublist


# Get input from the user
input_list = input("Enter a list of elements (separated by spaces): ").split()
input_list = [int(num) for num in input_list]

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

# Call the function
result = get_sublist(input_list, start_index, end_index)

# Print the result
print("Sub-list:", result)
