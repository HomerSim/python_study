# 현재 시간이 12시 부터 1시 이전이면 점심을 먹고
# 3시부터 4시 이거나 아프면 휴식하고
# 아니면 일을 한다
time = 12
seek = True
#if time >= 12 and time < 13:
if 12 <= time < 13 and not seek:
    print("점심 먹으러감")
elif 15 <= time <= 16 or seek:
    print("휴식시간임..")
else:
    print("일하는 중..")
    

name = "abcdef"

if "a" in name:
    print("있음")
else:
    print("없음")

name = ["홍길동", "가가멜", "가제트"]

if "가제트" not in name:
    print("없음")
else:
    print("있음")

#반복문 while

guest = 1

while guest < 10:
  
    print("손님이 {} 명입니다.".format(guest))
    guest = guest + 1

    if guest == 10:
        print("손님이 꽉 찼습니다")



num = 1 
jjak = 0
hol = 0
while num <= 10:
    if num % 2 == 0:
        print("짝 {}" . format(num))
        jjak += num
    else:
        print ("홀 {}" . format(num))
        hol += num

    num += 1


print("홀 합 {}" . format(hol))
print("짝 합 {}" . format(jjak))

# 반복문 for 

a = "abcdefg"
for i in a:
    print(i)

a = ['python', 'java', 'php', 'c', 'c++', 'javascript']

for i in a :
    print(i)


for i in range(1, 10, 2):
    print(i)


a= [(1,2), (3,4), (5,6)]

for i in a:
    print(i)
    for j in i:
        print(j)

a = [[[1,2,3,4,5], ['a','b','c'], [11,12,13,14]]]
for i in a:
    for j in i:
        print(j)


msg  = "python programing"
for s, i in enumerate(msg, start=1):
    print(s, i)

student = [{'홍길동':100}, {"가제트":200},{"가가멜":300}]
for s, i in enumerate(student):
    #print(i)
    data = list(i.items())[0]
    name = data[0]
    value = data[1]
    print("{}. 이름: {} 점수: {}" . format(s, name, value))


'''
result = []
for num in range(1, 6):
    result.append(num+5)
'''

result = [num + 5 for num in range(1,6)]
print(result)

result = [num + 5 for num in range(1, 10) if num % 2 == 0]
print(result)

for num in range(1, 99):
    if num % 2 == 0:
        result.append(num * 3)


for i in range(2, 10):
    for j in range(1, 10):
        result = i * j
        print("{} X {} = {}" .format(i,j, result))


gugudan = ["{} X {} = {}" . format(i,j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(gugudan)


# 반복문 while, for 

num = 0
for i in range(1, 1000):
    print(i)

    if i == 10:
        break


while True:
    print(num)
    num += 1

    if num == 10:
        break


print("========================")
num = 0
while num < 10:
    num+=1
    if num == 5:
        continue

    print(num)

print("========================")
point = [80,100,50,40,60]
for p in point:
    if p < 70:
        continue

    print("{}점 입니다". format(p))