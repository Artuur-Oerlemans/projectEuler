
counter = 0
for i in range(1, 100):
    for j in range(1, 10):
        if len(str(j ** i)) == i:
            print(i)
            counter += 1


print("The number n-digit positive integers which are also nth-power:", counter)