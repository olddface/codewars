def pos_average(s):
    totalThatEqual = 0#total nilai yang sama
    totalCom = 0#total kombinasi
    Arr = [i for i in (s.split(', '))]
    TotalNum = len(Arr) * len(Arr[0])#jumlah semua angkanya dari arr[0] -> terakhir
    '''jadi cara bertemuny
    s1 ama s2 atau index i ama index j ini supaya efisien 
    pakek i yang di mulai dari 1
    supaya urutanya:
    1[i:s1 dan j:s0] 
    2[i:s2 dan j:s0, i:s2 dan j:s1]
    3[i:s3 dan j:s0, i:s3 dan j:s1, i:s3 dan j:s2]
    dan seterusnya'''
    for i in range(1, len(Arr)):
        for j in range(i):
            totalCom+=1
            for x in range(len(Arr[0])):
                if Arr[i][x] == Arr[j][x]:
                    totalThatEqual+=1
    persentage = totalThatEqual * (100/TotalNum)#persentase nilai yang bener dari TotalNum
    last = format(persentage / totalCom * len(Arr), '.12g')
    return float(last)

print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))