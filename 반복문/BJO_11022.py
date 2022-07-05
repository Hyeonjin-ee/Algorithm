## A + B - 8
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
## 조건) 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력
import sys

N = int(input())

for i in range(1, N+1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i, A, B, A+B))