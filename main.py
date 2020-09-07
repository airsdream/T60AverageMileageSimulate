from repair import GetRepairDate, GetRepairTime

cycle = 10
times = 2
duration = 92

on_business = []

for i in range(cycle):
    on_business.append(GetRepairDate(duration,times))

print(on_business)
# a = GetRepairDate(92,times)
# b = GetRepairTime(1,7)
# for i in range(times):
#     if a[i] <= 31:
#         Oct += 1
#     elif a[i] <= 61:
#         Nov += 1
#     else:
#         Dec +=1
#     sum += 1
#
# OctPer = Oct / sum * 100
# NovPer = Nov / sum * 100
# DecPer = Dec / sum * 100
#
# print('Oct = %d , Nov = %d , Dec = %d'%(Oct,Nov,Dec))
# print('Oct = %.2f %%, Nov = %.2f %%, Dec = %.2f %%'%(OctPer,NovPer,DecPer))
# print(b)