import sys

input = sys.stdin.readline


def find_cheat(text1, text2, n1, n2):
    memory, result = [[0] * (n2 + 1) for _ in range(n1 + 1)], 0
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if text1[i] == text2[j]:
                memory[i][j] = 2 * (text1[i] == text2[j]) + memory[i + 1][j + 1]
            else:
                memory[i][j] = max(memory[i][j], memory[i + 1][j] - 1, memory[i][j + 1] - 1)
            result = max(result, memory[i][j])
    return result


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1, inputs2 = input(), input()
    print(find_cheat(inputs1, inputs2, inp1, inp2))
