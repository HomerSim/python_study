# 타이핑 게임 만들기

import time
import random
import os


'''
한글 = ((초성 * 21)+중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
'''
CHO = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]
JUNG = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
JONG = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]




def break_korean(string):
    word_list = list(string)
    break_word = []

    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            # 유니코드상 몇번째 글자인지 인덱스를 구합니다.
            char_index = ord(k) - ord('가')

            # 초성 = (유니코드인덱스 /28) /21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            # 중성 = (인덱스 /28) %21
            char2 = int((char_index / 28) % 21)
            break_word.append(JUNG[char2])

            # 종성 = 인덱스 % 28
            char3 = int(char_index % 28)

            if char3 > 0:
                break_word.append(JONG[char3])
        else:
            break_word.append(k)

    return break_word


WORD_LIST = [
"오 좋죠! 당신은 생명의 은인이에요.. 아뇨 아뇨.. 오늘도 괜찮아요. 바로 오세요.",
"정말 너무 고마워요. 그럼 있다 봬요.",
"누구 전화야?",
"론달씨요",
"론달이라..",
"왜 그 구직 세미나에서 만났던 선생님 있잖아요.",
"근데 왜 우리 집엔 온대?",
"지난 월요일 수업 끝나고서 같이 커피를 마셨는데",
"혹시 도움이 필요한...",
"잠깐, 거기서 멈춰봐. 론달이란 사람과 커피를 마셨다구?",
"그래요",
"나한텐 커피 마셨다는 그런 말 나한테 안 했었잖아",
"아 깜빡 했네요. 크림하고 설탕 두 스푼 넣은 커피였어요"
]
random.shuffle(WORD_LIST)



for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    src = break_korean(q)
    tar = break_korean(user_input)

    print(src)
    print(tar)

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break

        if c == src[i]:
            correct += 1

    tot_len = len(src)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed,c,e))
    os.system("pause")






user_input = input("입력 : ")
break_word = break_korean(user_input)

print("입력: {}".format(user_input))
print("분해: {}".format(break_word))
        



'''








'''

