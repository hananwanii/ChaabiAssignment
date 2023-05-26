def switch_keys_values(dictionary):
    return {value: key for key, value in dictionary.items()}


#You can use this function as follows:

input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result_dict = switch_keys_values(input_dict)
print(result_dict)
