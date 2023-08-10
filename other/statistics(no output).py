import statistics
import math

agesData=[10,13,14,12,11,10,11,10,15]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(statistics.sqrt(statistics.variance(agesData)))
