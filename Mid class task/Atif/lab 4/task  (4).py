def distinct(lst):
    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list


numbers = [1,2,3,3,3,3,4,5]

print(distinct(numbers))