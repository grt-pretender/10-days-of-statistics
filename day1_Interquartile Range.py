import statistics as stats

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

# calculating interquartile_range
S = []
for i in range(n):
    S += [X[i]] * F[i]
N = sum(F)
S.sort()

if n%2 != 0:
    quartile1 = stats.median(S[:N//2])
    quartile3 = stats.median(S[N//2+1:])
else:
    quartile1 = stats.median(S[:N//2])
    quartile3 = stats.median(S[N//2:])

interquartile_range = round(float(quartile3-quartile1), 1)
print(interquartile_range)
