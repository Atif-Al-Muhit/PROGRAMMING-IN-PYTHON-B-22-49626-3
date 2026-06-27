def count_elements(lst):
    for item in set(lst):
        print(item, "=>", lst.count(item))


numbers = [10,20,30,30,30,30,20,40]

count_elements(numbers)