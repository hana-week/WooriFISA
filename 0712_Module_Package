# 짝수만 걸러내기
list(filter(even, li)) # True 인 것만 체에 거르듯 조건을 만족시키는 값만 걸러지는 것

list(map(even, li)) # mapping 1:1 대응 : 정의역의 개수만큼 치역이 있다

li = [1, 2, 3, 4, 7]
# def even():
#     if :
#         return x
list(filter(lambda x: x % 2 == 0, li))

alist = ['사과', '바나나', '딸기', '오렌지'] # 4개
blist = ['Apple', 'Banana', 'Strawberry'] # 3개
clist = [100, 200, 300, 400, 500] # 5개

list(zip(blist, alist, clist))
# 더 작은 원소개수를 가진 집합자료 기준으로 zip 하기 때문에
# 누락되는 자료가 있을 수 있습니다. len()으로 원소개수 확인하세요.

# [변수에 적용할 수식 for 변수 in 이터러블 변수명]
[print(v1, v2[0], v2[1]) for v1, v2 in enumerate(zip(alist, blist))]
# [None, None, None] print 명령을 실행하기 때문

reduce(lambda x, y : x+y , array2dim)
# [[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
# []   [1]
# x    y
# x  +  y
        # [1]   [2, 2]
        # x    +  y
        # [1, 2, 2]  + [3, 3, 3]
            #   x    +     y
                #  x            +      y
            #   [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

print(li[:5]) # 1차원
reduce(lambda x, y : x+y , li)

# 2차원
test2 = [{'name' : 'a', 'age' : 1}, {'name' : 'b', 'age' : 2}, {'name' : 'c', 'age' : 3}]

reduce(lambda x, y : x+y['age'] , test2, 0) / len(test2) # 첫번째 x를 초기값 0 으로 설정
# 0 + test2[0]['age'] 1
#        1                 +   test2[1]['age']    2
#                           3                           +  test2[2]]['age'] 3

!pip install selenium # python index package

!pwd # print working directory

import sys # system 관련된 여러 설정들을 제어해주는 파이썬의 모듈

from modules.my_area2 import *   # 해당 모듈 안에 있는 함수를 다 가져옵니다

# 이 함수에는 처리할 수 있는 예외가 몇개나 존재할까요?
# 입력: '54321'
# 출력: 12345

def convert(a):
    return int(a[::-1])

import traceback # 에러메시지를 출력해주는 모듈입니다

def convert(a):
    if a.isdigit():
        return int(a[::-1])

try:
    print(convert(54321))
    print(convert('abcd'))
except:
    traceback.print_exc()

