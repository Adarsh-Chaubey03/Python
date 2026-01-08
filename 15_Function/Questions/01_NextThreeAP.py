# return next return an arithmetic progression tuple with its next three element
def extendAP(arr):
    arr=list(arr)
    d=arr[1]-arr[0]
    for _ in range(3):
        arr.append(arr[-1]+d)
    return tuple(arr)

arr = (2, 4, 6)
print(extendAP(arr))