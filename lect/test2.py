#사용자 입력 받기

# num1 = input("숫자1 : ")
# num2 = input("숫자2 : ")
# print(int(num1) + int(num2))

# langs = ['한국어', 'Enlgish']
# for i, l in enumerate(langs, start=1):
#     print("{}. {}".format(i, l))

# while True:
#     sel = input("언어를 선택하세요. >")
#     if not sel.isnumeric():
#         continue

#     sel = int(sel)
#     if 0 < sel < 3:
#         break

# print("사용자가 선택한 언어는 {} 입니다." . format(langs[sel-1]))

# 입력한 숫자가 소수인지



while True:
    num = input("2 이상의 숫자를 입력하세요>")
    if not num.isnumeric():
        continue

    num = int(num)

    if num < 2:
        continue

    break


prime_list = [False, False] + [True] * (num -1)
primes = []

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(2*i, num+1,i):
            prime_list[j] = False



primes = [i for i in range(2, num+1) if prime_list[i] == True]
print(primes)

if num in primes:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")
# isprime = True

# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break


# if isprime:
#     print("소수입니다.")
# else:
#     print("소수가 아닙니다.")







