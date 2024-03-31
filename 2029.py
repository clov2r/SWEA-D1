# SWEA D1
import math
test=int(input())
for i in range(test):
    a, b=map(int, input().split())
    result1= a/b
    result2= a%b
    print("#%d" %(i+1), math.floor(result1), result2)
# 변수 값을 출력하려면 "%d" %(변수명)
