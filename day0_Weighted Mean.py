n = int(input())
numbers = list(map(int,input().split()))
weights = list(map(int,input().split()))

# calculating weighted mean
numerator = sum(numbers[i] * weights[i] for i in range(n))
sum_of_weights = sum(weights)

weighted_mean = numerator / sum_of_weights
print(round(weighted_mean,1))