from repair import GetRepairDate, GetRepairTime
import random
import numpy as np
from matplotlib import pyplot as plt

cycle = 10000  #循环模拟次数
duration = 92   #每次模拟运营时长 （天）

times = 1   #车均维修次数
random_repair_times = True #是否开启随机维修次数
min_repair_times = 1    #随机最小维修次数
max_repair_times = 3    #随机最大维修次数

min_repair_days = 1 #最短维修时长（天）
max_repair_days = 3 #最长维修时长（天）

average_mileage = 13.5    #每日车均骑行里程 km
random_riding_mileage = True   #是否开启随机每日车均骑行里程
min_mileage = 10.0   #随机最小每日车均骑行里程 km
max_mileage = 15.0  #随机最大每日车均骑行里程 km

# 生成随机的维修日期及维修时长 #

repair_dates = []   #随机维修日期列表
repair_times = []   #一一对应的随机维修时长列表
repairs = []        #每次循环维修车辆次数的列表

for i in range(cycle):
    if random_repair_times:
        times = random.randint(min_repair_times,max_repair_times)
        repairs.append(times)
    repair_dates.append(GetRepairDate(duration,times))
    repair_times.append(GetRepairTime(min_repair_days,max_repair_days,times))
    for j in range(times):
        if j < times-1:
            while repair_dates[i][j] + repair_times[i][j] >= repair_dates[i][j+1]:  #检查维修日期加上维修时长超过下一次维修日期的数据
                #print('维修日期不合理',repair_dates[i],repair_times[i],'->',end='') #打印维修日期加上维修时长超过下一次维修日期的数据
                repair_dates[i] = GetRepairDate(duration,times) #重新生成维修日期
                #print(repair_dates[i],repair_times[i])  #打印新成圣的维修日期及上一次生成的维修时长
        else:
            if repair_dates[i][j] + repair_times[i][j] >= duration:
                #print('最后一次维修超出运营期限', repair_dates[i], repair_times[i],'->',end='')
                repair_times[i][j] = duration - repair_dates[i][j]
                #print(repair_times[i][j])
#print(repair_dates)
#print(repair_times)

# 计算运营的时长 #

on_business = []    #每次投放运营，该次运营的时长（天）
business_days = []  #所有循环模拟中，每次循环的平均运营时长列表

for i in range(cycle):
    last_date = duration
    on_business = []
    for j in range(len(repair_dates[i])-1,-1,-1):
        on_business.append(last_date - repair_dates[i][j] - repair_times[i][j])
        last_date = repair_dates[i][j]
    on_business.append(last_date)
    on_business.reverse()
    business_days.append(on_business)
#print(business_days)

# 计算每次循环中，每次投放运营的里程 #

mileage_per_cycle = []

for i in range(cycle):
    mileage_per_day = []
    for j in range(len(business_days[i])):
        if random_riding_mileage:
            average_mileage = random.uniform(min_mileage,max_mileage)
        average_mileage = round(average_mileage,3)
        mileage_per_day.append(business_days[i][j] * average_mileage)
    mileage_per_cycle.append(mileage_per_day)
#print(mileage_per_cycle)


# 计算每次循环的累计平均运营里程 #

success = 0 #累计车均里程达到500km以上的次数

accumulative_average_mileage_per_cycle = []
for i in range(cycle):
    accumulative_average_mileage_per_cycle.append(np.average(mileage_per_cycle[i]))
    if accumulative_average_mileage_per_cycle[i] >= 500:
        success += 1
#print(accumulative_average_mileage_per_cycle)


if random_repair_times:
    times = np.average(repairs)

print('累计模拟循环 = ',cycle)
print('平均维修次数 = ',times)
print('成功达到500km目标的概率 = %.2f %%'%(success/cycle*100))

# 划分横坐标分度值

bins = []
for i in range(0,(int(max(accumulative_average_mileage_per_cycle)) // 100 + 1) * 100 + 1,10):
    bins.append(i)

# 绘制直方图

#plt.hist(accumulative_average_mileage_per_cycle, bins= bins)
#plt.show()
