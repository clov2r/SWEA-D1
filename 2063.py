# SWEA D1
N = int(input())
scores = list(map(int, input().split()))
scores.sort()
median = scores[N // 2]
print(median)
