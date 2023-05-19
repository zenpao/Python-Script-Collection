report_list = [['#', 'Date', 'Time', 'Name', 'Adults', 'Children', 'Subtotal'],
               [1, 'Nov 20, 2020', '11:30 pm', 'Ella Fich', 1, 1, 800.0],
               [1, 'Nov 20, 2020', '11:30 pm', 'Ella Fich', 1, 2, 1100.0],
               [1, 'Nov 20, 2020', '11:30 pm', 'Ella Fich', 1, 2, 1100.0]]


for i in range(len(report_list)):
    for j in range(len(report_list[i])):
        print(report_list[i][j], end=" ")
    print()

#print(sum([i[4][1] for i in report_list])) #sum of adults
#print(sum([i[5][1] for i in report_list])) #sum of children
#print(sum([i[6][1] for i in report_list])) #sum of subtotal

sumAdults = 0
sumKids = 0
sumSubTotal = 0
ctr = len(report_list) - 1
ctr2 = 1
while ctr != 0:
    sumAdults += report_list[ctr2][4]
    sumKids += report_list[ctr2][5]
    sumSubTotal += report_list[ctr2][6]
    ctr -= 1
    ctr2 += 1

print(sumAdults)
print(sumKids)
print(sumSubTotal)