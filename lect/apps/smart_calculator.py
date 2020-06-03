# 계산기 업그레이드
# 5 + 5 * 10 순차적으로 계산
import os 



operator = ["+", "-", "*", "/", "="]


def string_calculator(user_input, shopw_history = False):

    string_list = []
    lop = 0

    if user_input[-1] not in operator:
        user_input += "="

    for i,s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i])
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1]

    # ['10', '+', '20', '+', '30']
    # ['10', '+', '20', '+', '30']
    # ['30', '+', '30']
    # ['60']

    pos = 0
    while True:
        if pos + 1 > len(string_list):
            break

        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos -1] + string_list[pos] + string_list[pos + 1]
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if shopw_history == True:
                print(string_list)
                
        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])
    
    return round(result,4)


while True:
    os.system("cls")
    user_input = input("계산식을 입력하세요 : ")
    if user_input == "/exit":
        break

    result = string_calculator(user_input, True)
    print("결과: {}" . format(result))
    os.system("pause")
