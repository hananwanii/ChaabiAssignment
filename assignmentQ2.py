def get_file_type(extension_type_list, filenames):
    type_dict = {}

    extension_type_pairs = extension_type_list.split(';')
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        type_dict[extension] = file_type

    result_dict = {}
    for filename in filenames:
        parts = filename.split('.')
        if len(parts) > 1:
            extension = parts[-1]
            if extension in type_dict:
                result_dict[filename] = type_dict[extension]
            else:
                result_dict[filename] = 'unknown'
        else:
            result_dict[filename] = 'unknown'

    return result_dict


# Get input from the user
extension_type_list = input("Enter extension and type values (e.g., xls,spreadsheet;xlsx,spreadsheet;jpg,image): ")
filenames = input("Enter a list of filenames (separated by spaces): ").split()

# Call the function
result = get_file_type(extension_type_list, filenames)

# Print the result
for filename, file_type in result.items():
    print(f"{filename}: {file_type}")
