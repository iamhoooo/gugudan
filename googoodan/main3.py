print("구구단 출력.\n")
Num_input = int(input("숫자를 입력하세요!"))
for i in range(1, 10):
    result = Num_input * 1
    print(Num_input,"*",i ,"=", result,"입니다.")

print("구구단 2단부터 9단까지 출력. \n")
for x in range(1, 10):
    for y in range(1, 10):
        print(x, "*", y, "=", x*y)