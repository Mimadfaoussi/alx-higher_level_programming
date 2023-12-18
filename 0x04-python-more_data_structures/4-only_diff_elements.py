#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for i in set_1:
        for j in set_2:
            if (i == j):
                common.add(i)
                break
    return (common)


def only_diff_elements(set_1, set_2):
    common = common_elements(set_1, set_2)
    diff = set()
    print(common)
    for elm, elm2 in zip(set_1, set_2):
        if elm not in common:
            diff.add(elm)
        if elm2 not in common:
            diff.add(elm2)
    return (diff)
