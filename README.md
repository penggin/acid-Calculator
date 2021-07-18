# 중화반응의 양적관계 계산기
이 프로젝트는 학교 화학과목의 세특을 위해 제작되었습니다. (20916 이동훈)

## 소개
+ 이 프로젝트는 Python 3.8.10 을 이용하여 제작되었습니다.
+ 에디터로는 VScode를 사용하였습니다.
+ 이 프로젝트는 세특 제출용으로, 목표하는 것을 만들기위한 탐구과정이 자세히 서술되어있습니다.
+ 학교 **정보** 과목의 **문제해결과 프로그래밍** 과목을 활용하여 제작되었습니다.
+ 화학 교과서의 176쪽 내용을 참고하였습니다.
+ Python이 설치되지 않은 환경에서의 실행을 위해, .exe 파일도 실행할수있도록 패키징 해두었습니다.

## 프로그램 실행방법

-----
## 문제분석
문제 : 우리는 학교 화학시간에 **역동적인 화학 반응**단원의 **1. 산 염기와 중화반응**에서 **중화 반응의 양적관계** 라는 부분에서 A물질의 `몰농도`, `양(부피)`, `가수(분자 1개가 내놓는 산 또는 염기의 수)` 와 B물질의 `몰농도`, `가수` 를 알고있을때, B물질을 A물질에 얼마나 넣어야 중화되는지 계산하는 방법을 배운적이 있다. 하지만 간단한 계산(수가 딱 떨어지는 계산) 을 제외하면 오래 걸린다.

### 문제의 이해와 분석
현재상태 : 간단한 수가 아닌 계산에서의 시간이 오래걸린다.

목표상태 : 복잡한 수가 입력되더라도, 빠르게 계산할수 있다.

필요한 정보 : A물질의 [몰농도, 양(부피), 가수], B물질의 [몰농도, 가수], 계산에 필요한 공식

### 문제의 분해
+ 어느 형식의 프로그램으로 만들어야 사용하기 편할까? (cli, gui)
+ 어떤 방식으로 계산을 해야할까?
+ 어느 순서로 프로그램이 실행되어야 할까?

### 문제의 구조화
어떤 순서로 프로그램이 실행되어야 할지 구조화 해 보았다.
![image](https://user-images.githubusercontent.com/77449586/126068677-c40baa46-ab26-430c-8ce2-7cba33b60390.png)

## 알고리즘
알고리즘에는 다섯가지의 조건이 있다.
1. 입력이 0개 이상일것
2. 출력이 1개 이상일것
3. 수행이 가능할것
4. 알고리즘이 명확할것
5. 알고리즘이 유한할것

위의 조건에 맞게 알고리즘을 짜볼것이다.

### 알고리즘 설계
먼저 의사코드로 먼저 구성을 한뒤, 순서도를 이용해서 구성해보자!!

만드려는 프로그램은 다음과 같은 순서로 동작할것이다.
1. A물질의 [몰 농도, 양(부피), 가수] 와 B물질의 [몰 농도, 가수] 를 입력받는다.
2. 계산 공식을 이용하여, A물질과 B물질이 중성이 되려면, B물질이 얼마나 필요한지 계산한다.
3. 계산한 내용을 출력한다.

(생각보단 간단하다!)

이제 위의 내용을 바탕으로 순서도를 그려보자.

순서도의 규칙은 다음과 같다.
![image](https://user-images.githubusercontent.com/77449586/126069109-e222bbe5-a6f3-4c88-8b39-c3c04e4e9fbe.png)

이제 순서도를 그려보자. 
![화학 (1)](https://user-images.githubusercontent.com/77449586/126070468-80a81f5a-796a-43b2-8d06-21d5cb05ac94.png)

이제 위의 순서도에 따라 코딩을 해볼것이다.

## 코드짜기
위의 내용들을 바탕으로, 코드를 짜 보도록 하자.

먼저 구하려는 값인 V' 를 쉽게 구하기 위해서, 좌변에 V' 만 남기고, 나머지는 다 우변으로 이항을 해보자.

>> V' = ( n * M * V ) / ( n' * M' )

이제 이것을 사용하여 값을 구하는 함수를 만들어보자.

해당 함수는 아래와 같다.
```python
# n(A물질의 가수), M(A물질의 몰농도), V(A물질의 양), n_p(n' 와 같으며, B물질의 가수), M_P(M'과 같으며, B물질의 몰농도) 를 인자로 받는 calc 라는 이름의 함수를 정의한다.
# 타입힌트로 각각의 매개변수들은 float(실수형) 임을 나타내었으며, 리턴값도 실수형이다.
def calc(n: float, M: float, V: float, n_p: float, M_p: float) -> float:
    V_p = (n * M * V) / (n_p * M_p) # 위에서 구한 공식에 받은 값들을 대입한다. 파이썬에서 '*' 는 곱하기, `/` 는 나누기를 뜻한다. (더하기 빼기는 같다.)
    return V_p # 위에서 구한 값을 반환한다. (여기에서 V_p 의 값은 B물질의 양이다.)
```

그리고, 값을 입력받는 함수도 만들어보자.
```python
def main():
    # 파이썬의 내장함수인 input()는 괄호안의 내용을 출력하고, 사용자의 값을 입력받는 함수이다. 이를 이용하여 값을 입력받는다.
    n = float(input("A물질의 가수를 입력해주세요. : "))
    M = float(input("A물질의 몰 농도를 입력해주세요. : "))  # 위와 같다.
    V = float(input("A물질의 양을 입력해주세요. : ")) # 위와 같다.
    n_p = float(input("B물질의 가수를 입력해주세요. : ")) # 위와 같다.
    M_p = float(input("B물질의 몰 농도를 입력해주세요. : ")) # 위와 같다.
    res = calc(n, M, V, n_p, M_p) # calc 함수(방금 만들었던 계산하는 함수)에 값들을 입력하고, 결괏값을 res에 담는다.
    print(f"두 물질을 섞을때, 중성이 되기위한 B물질의 양은 {res}ml 입니다.") # 결괏값을 출력한다. 파이썬의 기본함수인 print() 는 괄호안의 내용을 출력한다.
    while True: # 무한히 반복한다.
        isrestart = input("다른 값을 계산하시겠습니까? (y/n) : ") 
        if isrestart == 'y': # 만약 isrestart 가 y 라면
            main() # 자기자신을 호출하여 새로운 계산을 시작한다.
            return #함수를 빠져나간다.
        elif isrestart == 'n': # 만약 isrestart 가 n 이라면
            print("프로그램이 종료됩니다...")
            time.sleep(2) # 사용자가 프로그램이 종료되는 중임을 인지할수있도록, 2초간 기다린다.
            return
        else: # 위의 조건들이 모두 성립하지 않는다면
            print("옳지 않은 응답입니다. (y/n) 중 하나를 입력해주세요.")
```

위와 같이 짤수있다!!

이제 한번 테스트를 해보자!
![usingexample3](https://user-images.githubusercontent.com/77449586/126071743-01a3742c-5174-48f3-9505-c46eab108bcf.gif)

정상적으로 잘 작동되는것을 확인할수 있었다!!

## 느낀점
전에 학교에서 이 내용을 배웠을때, "음... 입력값이 복잡하면 푸는게 힘들겠네... 더 빠르게 계산할수있는 방법은 없을까?" 라는 생각이 들었고, 한번 이 내용으로 프로그램을 만들고 싶었다. 그래서 이 활동을 하며 만들어보았다.

이 활동을 하면서 이 주제에 대해 깊이있게 탐구해보고, 추가적인 내용을 더 찾아보면서 어떤 방법으로 어떻게 해야 더 편하고, 더 효율적인지 고민을 해 보면서 문제해결과정에 정보시간때 배운 내용들을 이용하여 구조화하며 생각해 보내 효율적인 방법이 나온것같았다. 정보시간에 배운 내용과, 화학시간에 배운 내용을 접목시키면서 해보니, 더 재미있었던것 같다.

순서도그리기와, 가장 효율적이고 최선의 방법을 생각하고 정하는 과정, 코드를 어떻게 구성하면 효율적으로 짤수 있을지 고민을 해 보며 조금 힘들긴 했지만, 다 만들고 나니 매우 뿌듯했다!

나중에 이 내용을 바탕으로 프로그래밍에 관심있는 친구에게 가르쳐 주어야 겠다.

**선생님 긴글 읽으시느라 수고하셨습니다!!**
