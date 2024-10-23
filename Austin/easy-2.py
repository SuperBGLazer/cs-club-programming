def sum_lists(list1, list2):
    if len(list1) != len(list2):
        print("Lists aren't same length")
        exit(1)
    
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

print(sum_lists([1,2,3], [9,8,7]))
