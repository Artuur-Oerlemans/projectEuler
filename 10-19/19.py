months= [31, 28, 31, 30,31,30,31,31,30,31,30,31]
monthsLeapYear = [31, 29, 31, 30,31,30,31,31,30,31,30,31]

# know jan 1 of 1900 is a monday, and mondays are 1 mod 7.
year = 1900+1
days = 1 + sum(monthsLeapYear)
numberOfMondays = 0

for y in range(0, 100):
	if year %4==0:
		currentMonths = monthsLeapYear
	else:
		currentMonths = months
	for m in range(0,12):
		if days %7 ==0:
			numberOfMondays +=1
		days += currentMonths[m]
	year += 1

print(numberOfMondays)
