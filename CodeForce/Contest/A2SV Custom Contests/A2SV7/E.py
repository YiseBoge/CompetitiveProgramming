def find_probability(a, b, c, d):
    prob1, prob2 = a / b, c / d
    total = 1 / (1 - (1 - prob1) * (1 - prob2))
    return str(total * prob1)


if __name__ == "__main__":
    inp = list(map(int, input().split()))
    print(find_probability(*inp))
