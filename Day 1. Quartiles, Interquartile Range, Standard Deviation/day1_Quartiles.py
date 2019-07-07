import statistics as stats
n = input()
numbers = sorted(int(val) for val in input().split())
middle = int(n)//2

# easy way using statistics module
print(int(stats.median(numbers[:middle])))
print(int(stats.median(numbers)))
print(int(stats.median(numbers[-middle:])))
