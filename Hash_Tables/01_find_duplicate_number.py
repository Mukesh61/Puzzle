'''
Given a list of number, find if there is duplicate  number.

input: [1, 7, 5, 3, 4, 1]
output: "yes,duplicate found" because 1 is 2 times.

input: [1, 7, 5, 3, 4]
output: "all unique value"

max number will be: 100

if you are using python, try not to use dictionary.

'''

input_data = [1, 7, 5, 3, 4, 1]

def search_duplicate(input_data_local):
    number_found_list = [0] * 101
    for item in input_data_local:
        if number_found_list[item]:
            return 'yes, duplicate found'
        number_found_list[item] = 1

    return 'all unique value'

print(search_duplicate(input_data))
