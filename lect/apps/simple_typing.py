# 타이핑 게임 만들기
import time
import random
import os

WORD_LIST = [
"Oh, great!",
"You're a lifesaver.",
"No, no, no, no, today is fine.",
"Come right over",
"Thank you so much.",
"I really appreciate this.",
"Okay. Bye-bye.",
"Who was that?",
"Rondall.",
"Ron-daall?",
"Yeah, y'know, the teacher from that job search seminar i've been taking.",
"Why's he coming over here?",
"Well, last Monday, after class, we were having coffee and he said that anybody who needed…",
"Time out.",
"Flag that play.",
"Y-you had coffee with Rondall?",
"Yeah.",
"You didn't tell me, didn't tell me about this coffee.",
"Oh, I'm sorry. It was cream, two sugars"
]
random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(user_input):
        if i >= len(q):
            break

        if c == q[i]:
            correct += 1

    tot_len = len(q)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("속도: {:0.2f} 정확도: {:0.2f} 오타율: {:0.2f}".format(speed,c,e))
    os.system("pause")









