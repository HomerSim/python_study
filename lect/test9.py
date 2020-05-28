# 데코레이터
# 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

# 파이썬에서 함수는 일급객체
# 클로저 사용
# 함수내 함수를 정의할 수 있음

import time

def time_checker(func):
    def inner_function(*args, **kwargs):
        
        start_time = time.time()
        result = func(*args, **kwargs)
        print(result)
        end_time = time.time()
        print("함수 {} 동작시간: {}".format(func.__name__, end_time - start_time))
        return result

    return inner_function 

@time_checker
def test1(a, b):
    for i in range(5):
        time.sleep(0.1)
    return a+b

c = test1(5,5)
print(c)

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

from functools import wraps 

def login_required(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인이 되지 않아 수행하지 못합니다.")
            return "로그인이 필요한 페이지 입니다"
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    '''로그인 테스트 함수 입니다.
    '''
    print("안녕")


def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}>{}</{}>".format(new_args, func(name), new_args)

        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return "방가웡" + msg

print(test("홍길동"))


print(login.__name__)
print(login.__doc__)
login()


#test1()
test2()

# def test():
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)

#     end_time = time.time() - start_time
#     print("함수 동작 시간: {}" .format(end_time))


# test()