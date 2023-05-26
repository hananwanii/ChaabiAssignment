def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements


# Example input
Mainstream = [
    "One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online",
    "Bleach", "Dragon Ball Z", "One Piece"
]
must_watch = [
    "Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate",
    "The Devil is a Part Timer!", "One Piece", "Attack On Titan"
]

# Call the function
common, non_common = compare_lists(Mainstream, must_watch)

# Print the result
print("Common elements:", common)
print("Non-common elements:", non_common)

