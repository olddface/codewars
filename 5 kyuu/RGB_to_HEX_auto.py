def rgb(r, g, b):
    arr = []
    jon = ""
    arr.insert(0, r)
    arr.insert(1, g)
    arr.insert(2, b)
    for i in range(len(arr)):
        if arr[i] > 254:
            jon += hex(255)[2:]
        elif arr[i] < 0:
            jon += '0' + hex(0)[2:]
        else:
            jon += hex(arr[i])[2:] if (len(hex(arr[i])[2:]) > 1) else '0' + hex(arr[i])[2:]
    return jon.upper()
print(rgb(23, 0,0))
