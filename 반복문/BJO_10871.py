## (브론즈 5) X보다 작은 수
## 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
## 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성
import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split())) # 수열 A에 대한 정의

for i in range(N):
   if A[i] < X: # i번째 값이 주어진 X보다 작을 때
       print(A[i], end=" ") # 값을 출력