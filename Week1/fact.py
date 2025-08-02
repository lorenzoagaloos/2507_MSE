def factorial():
    number = input("input value(Input Positive Integer Number):")
    n = int(number)

    if n < 0:
        return "Negative numbers not valid"

    elif 0 <= n <= 1:
        return 1

    else:
        output = 1
        for i in range(1, n + 1):
            print(", ",i)    
            output *= i # output = output *i
        return output
        # i = 1
        # while i <= n:
        #     print(", ", i)
        #     output *= i
        #     i += 1
        # return output

if __name__ == "__main__":
    ans = factorial()
    print("\n Factorial Output:", ans)
