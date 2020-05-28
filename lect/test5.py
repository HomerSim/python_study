# 사용자 함수 

def outer_function (func):
    def inner_function(*args, **kwargs):
        print("함수명: {}" . format(func.__name__))
        print("args: {}" . format(args))
        print("kwargs: {}" . format(kwargs))

        result = func(*args, **kwargs)
        print("result:{}" . format(result))
        return result

    return inner_function

def add(a,b):
    return a+b

f = outer_function(add)
f(10,20)

# c = 10
# def add(a, b):
#     global c
#     c = a + b
#     return c

# a = add(1,3)
# print(a,c )

# def get_input_user(msg, casting = int):
#     ''' 사용자에게 msg 를 출력하고 casting 형태를 확인하여 입력된 값을 리턴합니다. 
#     Args:
#         msg(str):input 시 출력할 문구 
#         casting(class):사용자에게 입력 받은 값의 자료형
    
#     Returns:
#         user(casting-value):사용자에게 입력받은 값
#     '''
#     while True:
#         try:
#             user = casting(input(msg))
#             return user
#         except:
#             continue

# def save_winner(*args):
#     print(args)

# def save_winner2(**kwargs):
#     print(kwargs)
#     if kwargs.get("name1"):
#         print(kwargs["name1"])

# def hi():
#     print("Hello")


#  def add(a,b):
#      return a+b

#  def cal(func, a,b):
#      print("결과 {}" . format(func(a,b)))

# cal(add, 1,5)

# hello = hi
# hello()

# save_winner("홍길동", "가가멜", "아즈라엘")
# save_winner2(name1="홍길동", name2="가가멜")




# user = get_input_user("사용자 이름을 입력하세요 >", str)
# age = get_input_user("사용자 나이를 입력하세요 >")

# print(user, age)


# def test1(num):
#     num += 10
#     print(num)

# def test2(lists):
#     lists.append('AAA')
#     print(lists)

# a= 50
# test1(a)

# a = []
# a.append("1234")
# test2(a)
# print(a)


