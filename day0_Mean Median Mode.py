n = int(input())
numbers = sorted(int(val) for val in input().split())
arr_size = len(numbers)

# calculating mean
sum_of_numbers = sum(numbers)
mean = sum_of_numbers / arr_size
print(mean)

# calculating median
middle = int(n / 2)
if n % 2:
    median = numbers[int((n + 1) / 2)]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2
print(median)

# calculating mode
mode = max(numbers,key=numbers.count)
print(mode)
