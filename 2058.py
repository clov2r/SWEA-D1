# SWEA D1
N = input()
result = 0  # 결과를 저장할 변수 초기화
for i in N:  # 문자열의 각 자릿수에 대해 반복
    result += int(i)  # 문자열을 정수형으로 변환하여 더함
print(result)  # 결과 출력
