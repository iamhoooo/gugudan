def ssosu():
    print(f"소수를 찾아보자! \n")
    Num_input = int(input("숫자를 입력하시오"))

    if Num_input > 1:
        for i in range(2, Num_input):
            if (Num_input % i) == 0:
                print(Num_input, "은(는)소수가 아닙니다.")
                break
        else:
            print(Num_input, "은(는) 소수입니다.")
    else:
        print(Num_input, "은(는) 소수가 아닙니다.")