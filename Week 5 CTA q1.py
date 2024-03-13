year_nums = int(input("Please input the number of years: "))
total_rain = 0

for i in range (1, year_nums+1):
    for j in range (1, 13):
        rain = float (input ("Please input the inches of rainfall for month " + str(j) +" of year " + str(i)+ " : "))
        total_rain += rain
total_months = year_nums * 12
average_rain = total_rain / total_months
print("Number of months: " + str(total_months))
print("total inches of rainfall: " + str(total_rain))
print("average rainfall per month: " + str(average_rain))