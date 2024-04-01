# SWEA D1
T=int(input())
for i in range(T):
    A, B=map(int, input().split())
    print("#%i"%(i+1), end=' ')
    if(A>B):
        print(">")
    elif(A==B):
        print("=")
    elif(A<B):
        print("<")
