from functools import reduce
from math import floor
import random
import datetime
#gregorian minutes a year = 525,949.2
AVG_AGE = 40
MINUTES_PER_YEAR = 525949.2
HOURS_PER_YEAR = MINUTES_PER_YEAR / 60
DAYS_PER_YEAR = HOURS_PER_YEAR / 24
WEEKS_PER_YEAR = DAYS_PER_YEAR / 7
MONTHS_PER_YEAR = DAYS_PER_YEAR / 30
YEARS_PER_YEAR = 1

INTERVALS = {"Minutes per Year":MINUTES_PER_YEAR,
             "Hours per Year": HOURS_PER_YEAR, 
             "Days per Year": DAYS_PER_YEAR, 
             "Weeks per Year": WEEKS_PER_YEAR, 
             "Months per Year": MONTHS_PER_YEAR,
             "Years per Year": YEARS_PER_YEAR
             }

def calc_exp(units, log=False):
    exp = {"total":0, "by_unit":[], "by_unit_additive":[]}
    unitsExp = 0
    current_total_unitsExp = 0

    units = floor(units)
    for i in range(1,units + 1):
        if exp["total"] == 0:
            unitsExp = i
        else:
            unitsExp = 1 / exp["total"]
        if log:
            print("{}: {} + {} = {}".format(i, exp["total"], unitsExp, exp["total"] + unitsExp))
        exp["by_unit"].append(unitsExp)

        current_total_unitsExp += unitsExp

        exp["by_unit_additive"].append(current_total_unitsExp)
        exp["total"] = exp["total"] + unitsExp
    return exp

def calc_minutes():
    life_minutes = floor(MINUTES_PER_YEAR * AVG_AGE)
    results = calc_exp(life_minutes)
    unit_data = results["by_unit"]
    total = results["total"]
    print(total)
    print(total / MINUTES_PER_YEAR)

def calc_interval(interval_name):
    interval = INTERVALS[interval_name]
    interval_unit = interval_name.split()[0]
    life_minutes = interval * AVG_AGE
    results = calc_exp(life_minutes)
    unit_data = results["by_unit"]
    unit_data_additive = results["by_unit_additive"]
    unit_data_in_years = list(map(lambda x: x / interval, unit_data))
    total_units = results["total"]
    total_units_in_years = total_units / interval


    print("\tTotal Units: " + str(total_units))
    print("\tTotal Units (Years): " + str(total_units_in_years))

    for i in range(len(unit_data_additive)):
        half = total_units / 2
        if unit_data_additive[i] >= half:
            print("\tAfter {} actual {} ({} years), you experience {} total relative {}.".format(i,interval_unit,i / interval,unit_data_additive[i],interval_unit.lower()))
            print("\tThis is {} years".format(unit_data_additive[i] / interval))
            break
    return results

def calc_relative_age(actual_age):
    interval = random.choice(list(INTERVALS.keys()))
    result = calc_exp(INTERVALS[interval])
    return result['total']


rel_age = calc_relative_age(78)
print(rel_age)

#for name, value in INTERVALS.items():
#    start = datetime.datetime.now()
#    print(name)
#    calc_interval(name)
#    end = datetime.datetime.now()
#    duration = end - start
#    print("-----Elapsed Time: {}-----\n".format(duration))

