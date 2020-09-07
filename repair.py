import random

def GetRepairTime (min_repair_time,max_repair_time):
    repair_time = random.randint(min_repair_time,max_repair_time)
    return repair_time

def GetRepairDate (duration,times):
    repair_date = []
    for i in range(times):
        repair_date.append(random.randint(1,duration))
    repair_date.sort()
    return repair_date

