coins = [200,100,50,20,10,5,2,1]

def numberOfWays(i, goal):
	if i >= len(coins):
		if goal == 0:
			return 1
		else:
			return 0
	ways = 0
	while goal >=0:
		ways += numberOfWays(i+1,goal)
		goal -= coins[i]
	return ways

print(numberOfWays(0,200))