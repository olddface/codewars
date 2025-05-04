def allocate_rooms(customers):
    ## Write code here
    customers = [i  for i in customers if i[0]<i[1]]
    AllocatedCust = []
    for i in range(len(customers)):
        for j in range(len(customers)):
            if i > 0:
                if i == j:
                    continue
                if customers[i][1] < customers[j][0]:
                    pass


allocate_rooms([(1,2),(2,4),(4,2),(3,6), (4, 6), (6, 4)])