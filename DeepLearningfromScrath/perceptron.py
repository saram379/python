import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1, x2):  #AND게이트랑은 가중치, 편향만 다름
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):  #AND게이트랑은 가중치, 편향만 다름
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

'''
퍼셉트론 : 다수의 신호를 입력 받아 하나의 신호를 출력
  | 입력신호(x1, x2)에 가중치(w1, w2)가 각각 곱해져 임계값(theta)를 넘으면 1, 작거나 같으면 0 --- x1*w1 + x2*w2 > theta  ==> 1
  | theta를 편향(b)으로 나타내기도 b = -theta, 계산결과 0을 넘으면 1 ------------------------------- x1*w1 + x2*w2 + b > 1  ==> 1
                                e.g.   x1,x2 -> w1, w2,  b
AND게이트: 두 입력이 1일 때만 1 출력    1, 1 -> 0.5, 0.5, -0.7 ==> 0.5+0.5-0.7 > 0 이므로 1 ---이렇게 4조건에 맞는 가중치와 편향을 찾아줘야함

NAND게이트: 두 입력이 1일 때만 0 출력   1, 1 -> -0.5, -0.5, 0.7 ==> -0.5-0.5+0.7 < 0 이므로 0

OR게이트: 두 입력이 0일 때만 0 출력     1, 1 -> 0.5, 0.5, -0.2 ==> 0.5+0.5-0.2 > 0 이므로 1 / 0,0 -> 0+0-0.2 < 0 이므로 0출력
'''

for x1 in range(2):
    for x2 in range(2):
        print(AND(x1,x2))
        x2 += 1
    x1 += 1

for x1 in range(2):
    for x2 in range(2):
        print(NAND(x1,x2))
        x2 += 1
    x1 += 1

for x1 in range(2):
    for x2 in range(2):
        print(OR(x1,x2))
        x2 += 1
    x1 += 1