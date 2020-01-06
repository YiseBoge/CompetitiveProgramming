import sys


def __compare(number1, number2):
    if len(number1) > len(number2):
        return 1
    elif len(number2) > len(number1):
        return -1
    else:
        i = 0
        while i < len(number1):
            if int(number1[i]) > int(number2[i]):
                return 1
            elif int(number2[i]) > int(number1[i]):
                return -1
            i += 1
    return 0


def __sort(number1, number2):
    bigger = number1
    smaller = number2
    if len(number1) > len(number2):
        bigger = number1
        smaller = number2
    elif len(number2) > len(number1):
        bigger = number2
        smaller = number1
    else:
        i = 0
        while i < len(number1):
            if int(number1[i]) > int(number2[i]):
                bigger = number1
                smaller = number2
            elif int(number2[i]) > int(number1[i]):
                bigger = number2
                smaller = number1
            i += 1
    return [smaller, bigger]


def __add_zeros(number, zeros):
    return number + (zeros * "0")


def __clean_zeros(number):
    i = 0
    while i < (len(number) - 1):
        if number[i] != "0":
            break
        i += 1
    return number[i:]


def __clean_negative(number):
    if number[0] == "-":
        return __clean_zeros(number[1:])
    return __clean_zeros(number)


def __increment(val, keep_extra=True):
    result = ""
    carry = 1
    for i in range(len(val) - 1, -1, -1):
        res = int(val[i]) + carry
        result = str(res % 10) + result
        carry = res // 10
        if i == 0 and carry != 0 and keep_extra:
            result = str(carry) + result
    return result


def __complement(val, length):
    result = ""
    for i in range(length):
        res = str(9 - int(val[-1 * (i + 1)])) if i < len(val) else "9"
        result = res + result
    return __increment(result, keep_extra=False)


def add(input1, input2):
    carry = 0
    result = ""
    len1 = len(input1)
    len2 = len(input2)

    i = 0
    while True:
        index1 = (len(input1) - i) - 1
        index2 = (len(input2) - i) - 1

        if i >= len1 and i >= len2:
            break
        elif i >= len2:
            res = str(int(input1[index1]) + carry)
            result = res[-1] + result
            carry = int(res[-2]) if len(res) > 1 else 0
        elif i >= len1:
            res = str(int(input2[index2]) + carry)
            result = res[-1] + result
            carry = int(res[-2]) if len(res) > 1 else 0
        else:
            res = str(int(input1[index1]) + int(input2[index2]) + carry)
            result = res[-1] + result
            carry = int(res[-2]) if len(res) > 1 else 0
        i += 1
    return "0" if result == "" else result


def subtract(big, small):
    result = add(big, __complement(small, len(big)))
    return __clean_zeros(result)


def multiply(big, small):
    result = "0"
    power = 0

    for s in range(len(small) - 1, -1, -1):
        res = ""
        carry = 0
        for b in range(len(big) - 1, -1, -1):
            r = (int(small[s]) * int(big[b])) + carry
            carry = r // 10
            res = str(r % 10) + res
        if carry != 0:
            res = str(carry) + res

        result = add(result, __add_zeros(res, power))
        power += 1
    return __clean_zeros(result)


def divide(big, small):
    result = "0"
    while __compare(big, small) >= 0:
        big = subtract(big, small)
        result = __increment(result)

    result = result + "."
    for i in range(3):
        if big == "0":
            break
        big = big + "0"
        r = "0"
        while __compare(big, small) >= 0:
            big = subtract(big, small)
            r = __increment(r)
        result = result + r

    return __clean_zeros(result)


def cut_num(number: str, divisor: str):
    for i in range(1, len(number)):
        cut_string = number[:i]
        remaining_string = number[i:]

        if int(cut_string) >= int(divisor):
            return cut_string, remaining_string

    return number, ""


def long_divide(numerator: str, denominator: str, result: str):
    if int(numerator) < int(denominator):
        return result, numerator

    cut_number, remaining = cut_num(numerator, denominator)

    print(cut_num, remaining)

    quotient = int(cut_number) // int(denominator)
    reminder = int(cut_number) % int(denominator)

    result += str(quotient)
    remaining = str(reminder) + remaining
    return long_divide(remaining, denominator, result)


def solution(in1, operator, in2):
    # return __complement(in1, 5)
    # return __increment(in1)
    # return __sort(in1, in2)
    # return __compare(in1, in2)
    # return add(in1, in2)
    # return subtract(in1, in2)
    # return multiply(in1, in2)
    # return divide(in1, in2)

    negative1 = in1[0] == "-"
    negative2 = in2[0] == "-"
    negative_result = False

    clean1 = __clean_negative(in1)
    clean2 = __clean_negative(in2)
    sorted_nums = __sort(clean1, clean2)
    big = sorted_nums[1]
    small = sorted_nums[0]
    result = ""
    text = "Result: "

    if operator == "+":
        text = "Sum: "
        if not negative1 and not negative2:
            result = add(big, small)
        elif negative1 and negative2:
            negative_result = True
            result = add(big, small)
        elif negative1:
            negative_result = __compare(clean1, clean2) > 0
            result = subtract(big, small)
        elif negative2:
            negative_result = __compare(clean1, clean2) < 0
            result = subtract(big, small)
    elif operator == "-":
        text = "Difference: "
        if not negative1 and not negative2:
            negative_result = __compare(clean1, clean2) < 0
            result = subtract(big, small)
        elif negative1 and negative2:
            negative_result = __compare(clean1, clean2) > 0
            result = subtract(big, small)
        elif negative1:
            negative_result = True
            result = add(big, small)
        elif negative2:
            result = add(big, small)
    if operator == "*":
        text = "Product: "
        negative_result = (negative1 and not negative2) or (negative2 and not negative1)
        if clean1 == "0" or clean2 == "0":
            result = "0"
        else:
            result = multiply(big, small)
    if operator == "/":
        negative_result = (negative1 and not negative2) or (negative2 and not negative1)
        if clean2 == "0":
            result = "undefined"
        else:
            result = divide(clean1, clean2)

    if negative_result and result != "0":
        result = "-" + result

    return text + result


def main():
    print("Welcome...\n"
          "Input any operation using '+', '-', '*', '/'. Use 'exit' to leave."
          "\nFeel free to use negatives, but make sure to separate operator by spaces.")
    while True:
        print("\n> ", end="")
        try:
            inp = sys.stdin.readline().split()
            if inp == "exit":
                break
            in1 = inp[0]
            in2 = inp[1]
            in3 = inp[2]
            sys.stdout.write(str(solution(in1, in2, in3)))
        except:
            print("Sth went wrong, please try again.")

    print("It was nice while it lasted.")


if __name__ == "__main__":
    main()
