## (브론즈 5) A + B - 4
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break

## 깨달은 점 :
## stop조건이 명확하게 제시되어 있지 않아서 한참 생각했다.
## try ~ except문을 사용해 값을 입력받았을 때만 출력이 이루어지도록 했다.