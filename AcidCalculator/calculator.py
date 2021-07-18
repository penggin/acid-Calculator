import time

# n(A물질의 가수), M(A물질의 몰농도), V(A물질의 양), n_p(n' 와 같으며, B물질의 가수), M_P(M'과 같으며, B물질의 몰농도) 를 인자로 받는 calc 라는 이름의 함수를 정의한다.
# 타입힌트로 각각의 매개변수들은 float(실수형) 임을 나타내었으며, 리턴값도 실수형이다.


def calc(n: float, M: float, V: float, n_p: float, M_p: float) -> float:
    # 위에서 구한 공식에 받은 값들을 대입한다. 파이썬에서 '*' 는 곱하기, `/` 는 나누기를 뜻한다. (더하기 빼기는 같다.)
    V_p = (n * M * V) / (n_p * M_p)
    return V_p  # 위에서 구한 값을 반환한다. (여기에서 V_p 의 값은 B물질의 양이다.)


def main():
    # 파이썬의 내장함수인 input()는 괄호안의 내용을 출력하고, 사용자의 값을 입력받는 함수이다. 이를 이용하여 값을 입력받는다.
    n = float(input("A물질의 가수를 입력해주세요. : "))
    M = float(input("A물질의 몰 농도를 입력해주세요. : "))  # 위와 같다.
    V = float(input("A물질의 양을 입력해주세요. : "))  # 위와 같다.
    n_p = float(input("B물질의 가수를 입력해주세요. : "))  # 위와 같다.
    M_p = float(input("B물질의 몰 농도를 입력해주세요. : "))  # 위와 같다.
    # calc 함수(방금 만들었던 계산하는 함수)에 값들을 입력하고, 결괏값을 res에 담는다.
    res = calc(n, M, V, n_p, M_p)
    # 결괏값을 출력한다. 파이썬의 기본함수인 print() 는 괄호안의 내용을 출력한다.
    print(f"두 물질을 섞을때, 중성이 되기위한 B물질의 양은 {res}ml 입니다.")
    while True:  # 무한히 반복한다.
        isrestart = input("다른 값을 계산하시겠습니까? (y/n) : ")
        if isrestart == 'y':  # 만약 isrestart 가 y 라면
            main()  # 자기자신을 호출하여 새로운 계산을 시작한다.
            return  # 함수를 빠져나간다.
        elif isrestart == 'n':  # 만약 isrestart 가 n 이라면
            print("프로그램이 종료됩니다...")
            time.sleep(2)  # 사용자가 프로그램이 종료되는 중임을 인지할수있도록, 2초간 기다린다.
            return
        else:  # 위의 조건들이 모두 성립하지 않는다면
            print("옳지 않은 응답입니다. (y/n) 중 하나를 입력해주세요.")


main()
#1, 0.1, 100, 1, 0.1
