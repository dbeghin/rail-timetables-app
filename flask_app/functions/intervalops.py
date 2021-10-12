def getPowerSet(llist):
    power_set_size = pow(2, len(llist))
    
    power_set=[]
    for iPower in range(1, power_set_size):
        subset = []
        for iSet in range(0, len(llist)):
            if (iPower & (1 << iSet)) > 0:
                subset.append(llist[iSet])
        if subset != []: power_set.append(subset)
    return power_set



def mergeIntervals(interval1, interval2):
    interval_out = []
    merge_successful = False
    lmin = 0
    rmin = 0
    lmax = 0
    rmax = 0
    if interval1[0] <= interval2[0]:
        lmin = interval1[0]
        rmin = interval1[1]
        lmax = interval2[0]
        rmax = interval2[1]
    else:
        lmin = interval2[0]
        rmin = interval2[1]
        lmax = interval1[0]
        rmax = interval1[1]

    if lmin <= lmax <= rmin <= rmax:
        interval_out = [lmin, rmax]
        merge_successful = True
    elif lmin <= lmax <= rmax <= rmin:
        interval_out = [lmin, rmin]
        merge_successful = True
    else:
        merge_successful = False

    output = [merge_successful, interval_out]
    return output


def mergeIntervalsInList(list_of_intervals):
    list_cleaned = []
    list_copy=list_of_intervals.copy()
    iInd1 = 0
    while iInd1 < len(list_copy):
        interval1 = list_copy[iInd1]
            
        iInd2 = iInd1 + 1
        bMerge = False
        while iInd2 < len(list_copy):
            interval2 = list_copy[iInd2]
            merging = mergeIntervals(interval1, interval2)

            if merging[0]:
                list_copy[iInd1] = merging[1]
                list_copy.pop(iInd2)
                bMerge = True
                break
            else:
                iInd2 += 1

        if not bMerge or iInd1 == len(list_copy)-1:
            list_cleaned.append(list_copy[iInd1])
            iInd1 += 1
    list_cleaned = sorted(list_cleaned, key=lambda r: r[0])
    return list_cleaned


def belongsToInterval(number, list_of_intervals):
    belongs = False
    for interval in list_of_intervals:
        if interval[0] <= number <= interval[1]:
            belongs = True
            break
    return belongs



def addToPowerRange(old_power_range, new_element):
    new_power_range = old_power_range.copy()
    for new_sub_range in new_element:
        new_power_range.append(new_sub_range)
        for old_sub_range in old_power_range:
            sum_min = old_sub_range[0] + new_sub_range[0]
            sum_max = old_sub_range[1] + new_sub_range[1]
            new_power_range.append([sum_min, sum_max])
    cleaned_power_range = mergeIntervalsInList(new_power_range)
    return cleaned_power_range



def getMaxPower(power_range):
    max_power = 0
    if len(power_range) > 0:
        last_element = power_range[-1]
        max_power = last_element[1]
    return max_power


def getMinPower(power_range):
    min_power = 0
    if len(power_range) > 0:
        first_element = power_range[0]
        min_power = first_element[0]
    return min_power


def reduceRangeBy(power_range, number):
    subtracted_range = []
    for tmp_ran in power_range:
        sub_min = tmp_ran[0] - number
        if sub_min < 0: sub_min = 0
        sub_max = tmp_ran[1] - number
        if sub_max < 0: sub_max = 0
        
        subtracted_range.append([sub_min, sub_max])
    return subtracted_range
