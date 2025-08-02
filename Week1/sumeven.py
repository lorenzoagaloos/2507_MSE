def SumEvenNumbers():
    number = input("input value(Input Positive Number):")
    n = int(number)

    if n < 0:
        return "Negative numbers not valid"

    elif 0 <= n <= 1:
        return 2

    else:
        output = 0
        i = 0
        while i <= n:
            print(", ", i)
            output += i
            i += 2
        return output

if __name__ == "__main__":
    ans = SumEvenNumbers()
    print("\n Sum of even numbers:", ans)