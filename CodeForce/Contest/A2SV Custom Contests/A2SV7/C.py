def count_moves(r1, c1, r2, c2):
    small, big = list(sorted([abs(r1 - r2), abs(c1 - c2)]))
    result = [str(int((small != 0) + 1)),
              "0" if (r1 + c1) % 2 != (r2 + c2) % 2 else str(2 - (small == big)),
              str(big)]
    return " ".join(result)


if __name__ == "__main__":
    inp = list(map(int, input().split()))
    print(count_moves(*inp))
