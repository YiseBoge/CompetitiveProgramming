def check(step, n, target):
    current = 0
    while current < n - 1:
        current = current + step[current]
        if current == target - 1:
            return "YES"
    return "NO"


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs = list(map(int, input().split()))
    print(check(inputs, inp1, inp2))
