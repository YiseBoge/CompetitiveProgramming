def make_num(r, g, b):
    balloons = list(sorted([r, g, b]))
    start, end = 1, balloons[-1]
    while start <= end:
        mid = (start + end) // 2

        rounds, rem = divmod(balloons[2], mid)
        rounds, rem = (rounds, rem) if rounds < 2 else (2, 0)

        needed = mid - rem
        temp = balloons[1] - min(needed, balloons[1])
        rem += balloons[1]
        if rem >= mid:
            rounds, rem = rounds + 1, 0

        if temp:
            rounds2, rem = divmod(temp, mid)
            rounds += rounds2
        rounds, rem = (rounds, rem) if rounds < 3 else (3, 0)

        needed = mid - rem
        temp = balloons[0] - min(needed, balloons[0])
        rem += balloons[0]
        if rem >= mid:
            rounds, rem = rounds + 1, 0

        if temp:
            rounds3, rem = divmod(temp, mid)
            rounds += rounds3
        rounds, rem = (rounds, rem) if rounds < 3 else (3, 0)

        if rounds == 3:
            start = mid + 1
        else:
            end = mid - 1
    return end


if __name__ == "__main__":
    inp1, inp2, inp3 = list(map(int, input().split()))
    print(make_num(inp1, inp2, inp3))
