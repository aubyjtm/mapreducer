
import sys

# -- Airline Data
# Year, Month, DayofMonth, DayOfWeek, DepTime, CRSDepTime, ArrTime, CRSArrTime, UniqueCarrier, FlightNum,
# TailNum, ActualElapsedTime, CRSElapsedTime, AirTime, ArrDelay, DepDelay, Origin, Dest, Distance, TaxiIn,
# TaxiOut, Cancelled, CancellationCode, Diverted, CarrierDelay, WeatherDelay, NASDelay, SecurityDelay, LateAircraftDelay
# print(sys.argv)
# print(sys.stdin)
reduceDict ={}
for line in sys.stdin:
    line = line.strip()
    Origin, Cancelled = line.split(",")
    Cancelled = int(Cancelled)
    if Origin not in reduceDict:
        reduceDict[Origin] = {"Total": 0, "Cancelled": 0}
        if Cancelled:
            reduceDict[Origin]["Cancelled"] = 1
    if Origin in reduceDict:
        reduceDict[Origin]["Total"] +=1
        if Cancelled:
            reduceDict[Origin]["Cancelled"] += 1
    # print("\t".join(results))
# for key in reduceDict:
#     if reduceDict[key]["Cancelled"]:
#         print(key,reduceDict[key])
# print(reduceDict)
output = [",".join([str(k),str(v["Cancelled"]),str(v["Total"])]) for k,v in reduceDict.items()]
# print("\n".join(output))
# print("\n".join(reduceDict))
    
with open("reducedResulst.csv","w+") as f:
    f.write("\n".join(output))
