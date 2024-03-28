# SWEA D1
a=int(input()) # 입력 받은 값 만큼 모두 더하라
result=0
for i in range(1, a+1): #1부터 a까지의 숫자를 반환한다 > i는 1부터 a까지의 숫자를 가짐
    result+=i # result 변수에 i 값을 더함 < 현재까지의 누적된 합을 저장
print(result) 
