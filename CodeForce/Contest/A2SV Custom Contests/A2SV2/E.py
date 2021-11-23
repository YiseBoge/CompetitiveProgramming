from collections import Counter


def find_palindrome(string):
    counts, n = Counter(string), len(string)
    for c, count in counts.items():
        if count >= 100:
            return c * 100

    lefts, rights = [[-1] * 26 for _ in range(n + 1)], [[n] * 26 for _ in range(n + 1)]
    for i in range(n):
        j = n - 1 - i
        for ind in range(26):
            lefts[i + 1][ind] = lefts[i][ind]
            rights[j][ind] = rights[j + 1][ind]
        left_ind, right_ind = ord(string[i]) - ord("a"), ord(string[j]) - ord("a")
        lefts[i + 1][left_ind], rights[j][right_ind] = i, j

    memory = {}

    def find(start, end, seen=0):
        nonlocal string, memory
        state = (start, end)
        if state not in memory:
            memory[state] = ""
            if seen < 100:
                for c_ind in range(26):
                    left, right = rights[start][c_ind], lefts[end + 1][c_ind]
                    if left == right:
                        memory[state] = max(memory[state], string[left], key=len)
                    elif left < right:
                        res = string[left] + find(left + 1, right - 1, seen + 2) + string[right]
                        memory[state] = max(memory[state], res, key=len)
                    if len(memory[state]) == 100 - seen:
                        break
        return memory[state]

    return find(0, len(string) - 1)


# def find_palindrome(string):
#     counts = Counter(string)
#     for c, count in counts.items():
#         if count >= 100:
#             return c * 100
#     memory = {}
#
#     def find(start, end, seen=0):
#         nonlocal string, memory
#         state = (start, end)
#         if start >= end or seen == 100:
#             return string[start] if start == end else ""
#         if state not in memory:
#             memory[state] = ""
#             if string[start] == string[end]:
#                 memory[state] = string[start] + find(start + 1, end - 1, seen + 2) + string[end]
#             else:
#                 memory[state] = find(start + 1, end, seen)
#                 if len(memory[state]) != 100 - seen:
#                     memory[state] = max(memory[state], find(start, end - 1, seen), key=len)
#         return memory[state]
#     return find(0, len(string) - 1)


if __name__ == "__main__":
    print(find_palindrome(input()))
