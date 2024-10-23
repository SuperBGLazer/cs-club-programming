def odd_index(arr):
    result = []
    for i in range(len(arr)):
        if i % 2:
            result.append(arr[i])
    return result

print(odd_index([1, 5, 2, 9, 12]))
