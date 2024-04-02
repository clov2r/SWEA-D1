# SWEA D1
X=int(input()) # 넣고 싶은 숫자 넣음
X_list=[] # for문 돌리기 전에 리스트 생성
for i in range(X+1):
    X_list.append(i) #list 안에 i 값을 넣어야 풀려서 append() 사용
X_list.reverse() # reverse() 사용해서 거꾸로 출력될 수 있게 만듦
print(*X_list) # 대괄호 빼고 리스트 안에 있는 요소들만 뽑고 싶어서 * 붙임
