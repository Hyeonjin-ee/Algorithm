## (브론즈 5) A + B - 5
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
## 입력의 마지막에는 0 두 개가 들어온다.
import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if(A == B == 0):
        break
    print(A+B)

## 꺠달은 점 :
## 입력값이 모두 0일 때, 실행을 멈춰야한다는 조건을 보고
## 처음에는 if문만 사용하면 된다고 생각했는데 원하는 방향과 조금 다르다는 것을 알고
## while 무한루프 속에 if문을 넣어서 0,0을 입력받았을 때 break가 되도록 바꾸었다.