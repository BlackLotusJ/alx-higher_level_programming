#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0,len(my_list)):
        if idx < 0 or idx > len(my_list):
            return None
        else:
            print("{:d}".format(my_list[i]))