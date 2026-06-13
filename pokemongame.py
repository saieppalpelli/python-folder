powers = [1,4,6,8]
mini = maxi = powers[0]
print(mini, maxi)

for power in powers[1:]:
    mini = min(mini, power)
    maxi = max(maxi, power)
    print(mini, maxi)