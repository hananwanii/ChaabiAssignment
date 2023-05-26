def sort_list_of_dicts(list_of_dicts, sort_key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list


# Get input from the user
list_of_dicts = []
while True:
    fruit = input("Enter the fruit name (or press Enter to stop): ")
    if fruit == "":
        break
    color = input("Enter the color: ")
    list_of_dicts.append({"fruit": fruit, "color": color})

sort_key = input("Enter the key to sort the list (fruit or color): ")

# Call the function
sorted_list = sort_list_of_dicts(list_of_dicts, sort_key)

# Print the result
for item in sorted_list:
    print(item)
