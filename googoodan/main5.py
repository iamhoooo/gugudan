print(f"입력한 숫자 안에 있는 모든 소수를 찾아보자")

num = int(input("숫자입력해라"))

#for j in range(0, num-1):
#    for i in range(2, num):
#        if(num-j % i == 0): #소수가 아닐때
#            break
#        else:
#            print(num-j, "은(는)소수 입니다.")

for i in range(2, num):
    s = 0
    for j in range(1, i):
        if (j == 1): continue

        if (i % j == 0): #소수가 아님
            s = 1
            break
    if (s == 0):
        print(i,end=' ')
