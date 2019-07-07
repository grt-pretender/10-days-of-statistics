import math

n = int(input())
numbers = list(map(int, input().split(' ')))

# calculating mean
arr_size = len(numbers)
sum_of_numbers = sum(numbers)
mean = sum_of_numbers / arr_size

print(math.sqrt(sum([(numbers[i] - mean) ** 2 for i in range(n)]) / n))
