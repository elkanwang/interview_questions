def  getMinTimeDifference( times):
    def formulate(time):
        time = time.split(":")
        if int(time[0]) == 24:
            time[0] = 0
        print time
        return int(time[0])*60 + int(time[1])
    times = map(formulate, times)
    times.sort()
    minTime = 24*60
    for i in range(1,len(times)):
        minTime = min(minTime, times[i]-times[i-1])
    minTime = min(minTime, times[0]+24*60-times[-1])
    return minTime

# print getMinTimeDifference(["10:00", "19:20","06:45"])


import operator
def  getSuspiciousList( transactions):
    transactions = map(lambda x : x.split("|"), transactions)
    res = {}
    record = {}

    for transaction in transactions:
        # print transaction, res
        if transaction[0] in record:
            name = transaction[0]
            if transaction[2] != record[name][2] and int(transaction[3]) - int(record[name][3]) < 60:
                if transaction[0] not in res:
                    res[transaction[0]] = int(record[name][3])
        if int(transaction[1]) > 3000:
            if transaction[0] not in res:
                res[transaction[0]] = int(transaction[3])

        record[transaction[0]] = transaction
    sorted_res = sorted(res.items(), key=operator.itemgetter(1))
    return map(lambda x: x[0], sorted_res)
record = ["Shilpa|500|California|63",
"Tom|25|New York|615",
"Krasi|9000|California|1230",
"Tom|25|New York|1235",
"Tom|25|New York|1238",
"Shilpa|50|Michigan|1300",
"Matt|90000|Georgia|1305",
"Jay|100000|Virginia|1310",
"Krasi|49|Florida|1320",
"Krasi|83|California|1325",
"Shilpa|50|California|1350"]
print getSuspiciousList(record)
