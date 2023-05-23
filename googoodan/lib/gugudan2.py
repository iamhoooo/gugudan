def gugudan2():    
    num = int(input("구구단을 출력할 숫자를 입력하세요 "))

    while num < 1:
        num = int(input("잘못된 입력입니다. 양수의 숫자를 입력하세요"))

    print(f"{num}단을 출력합니다. \n")

    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")