#Question 2
data = open('CupcakeInvoices.csv')

# # #Question 3
# for row in data:
#     print(row)
# # #Question 4  
#     line = row.split(',')
#     print(line[2])
# # # Question 5
    # total = int(line[3]) * float(line[4])
    # print(total)
# # # Question 6
# total = 0
# for row in data:
#     line = row.split(',')
#     total += (int(line[3]) * float(line[4]))
#     rounded = round(total, 2)
#     print(rounded)

# data.close()

import matplotlib.pyplot as plt


plt.bar([1,2,3], [4,5,6])

plt.show()

chocolate_total = 0
strawberry_total = 0
vanilla_total = 0

for row in data:
    line = row.split(',')
    subtotals = (int(line[3]) * float(line[4]))
if row._contains_("Strawberry"):
    strawberry_total += subtotals
if row._contains_("Vanilla"):
    vanilla_total += subtotals
if row._contains_("Chocolate"):
    chocolate_total += subtotals
