#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(0, len(my_list)):
        if idx < 0 or idx < len(my_list) - 1:
            return 'None'
        else:
            return element = my_list[idx]
