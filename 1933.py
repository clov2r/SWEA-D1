# SWEA D1
N=int(input())
for i in range(N):
    """
냅다 N%i 처리하면 ZeroDivisionError 터져서 예외처리를 사용해 작성함
근데 예외처리 너무 오랜만에 써봐서 따로 노션에 정리함
    """
    try:
        if N%i==0:
            print(i, end=' ')
    except ZeroDivisionError: # 예외가 발생했을 때 어떠한 결과도 내고 싶지 않으면 pass 사용
        pass
print(N)
