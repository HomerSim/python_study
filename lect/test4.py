# 파이썬 예외 처리 try / except

try:
    # val = "10.5"
    # n = int(val)
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류 발생 {}" . format(e))


try:
    file = open("sample.txt", "r")
    n = "10"
    v = int(n)
except:
    print("오류발생")
else:
    print("정상 동작확인")
finally:
    file.close()
    print("파이널리 호출")
