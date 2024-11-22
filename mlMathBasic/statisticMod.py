# Using Python Statistics Module Get -> Mean, Median, Mode, Variance, Standard Deviation, and Range
import statistics as stat

data = [2,3,4,5,8,9,32]

mean_val = stat.mean(data)
print("Mean-", mean_val)

median_val = stat.median(data)
print("Median:-", median_val)

mode_val = stat.mode(data)
print("Mode:-", mode_val)

var_val = stat.variance(data)
print("Variance:-", var_val)

std_val = stat.stdev(data)
print("Standard Deviation:-", std_val)

range_val = max(data) - min(data)
print("Range:-", range_val)
