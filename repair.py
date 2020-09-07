import random

def GetRepairTime (min_repair_time,max_repair_time,times):
    repair_time = []
    for i in range(times):
        repair_time.append(random.randint(min_repair_time,max_repair_time))
    return repair_time

def GetRandomRepairDate (duration,times):
    repair_date = []
    for i in range(times):
        repair_date.append(random.randint(1,duration))
    return repair_date

def GetRepairDate (duration,times): #在一段时间内随机挑选指定数量的检修日期
    repair_date = GetRandomRepairDate(duration,times)
    while len(set(repair_date)) != len(repair_date):    #检查是否有重复日期
        #print('repeat ',' ',repair_date,end='->') #遇到重复的打印出来
        del repair_date[:]  #删除这次生成的检修日期
        repair_date = GetRandomRepairDate(duration,times)
        #print(repair_date) #打印重新生成修正后的日期
    repair_date.sort()  #从小到大排序
    return repair_date


