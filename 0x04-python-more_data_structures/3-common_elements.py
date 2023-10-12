#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set_1 & set_2
    return c_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
