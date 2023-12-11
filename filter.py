def filterRange(arr,a,b):
    return list(filter(lambda c:c>=a and c<=b,arr))

arr = [5, 3, 8, 1]

filtered = filterRange(arr, 1, 4)

print( filtered ) # 3,1 (matching values)

print( arr ) #5,3,8,1 (not modified)