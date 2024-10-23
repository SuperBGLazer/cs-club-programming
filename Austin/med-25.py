def monotonic(arr):
    prev=None
    ascending=None
    for el in arr:
        if prev is None and ascending is None:
            prev = el
            continue
        elif ascending is None:
            if el == prev + 1:
                ascending = True
            elif el == prev - 1:
                ascending = False
            else:
                return False
            prev = el
            continue
        
        if ascending:
            if el != prev + 1:
                return False
        else:
            if el != prev - 1:
                return False

        prev = el
    return True

print(monotonic([1,2,3,4]))
print(monotonic([1,2,4,4]))
print(monotonic([4,3,2,1]))
print(monotonic([-1,-2,-3,-4]))
