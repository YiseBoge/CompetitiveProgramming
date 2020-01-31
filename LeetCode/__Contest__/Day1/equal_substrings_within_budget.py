class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0
        start = 0
        count = 0

        for i in range(len(t)):
            added_cost = abs(ord(s[i]) - ord(t[i]))
            # print("Adding", count, i, added_cost)
            count += added_cost

            while count > maxCost:
                reduced_cost = abs(ord(s[start]) - ord(t[start]))
                # print("Removing", count, i, reduced_cost)
                count -= reduced_cost
                start += 1

            length = i - start + 1
            if length > result:
                result = length
        return result


def solution(l1, l2, l3):
    s = Solution()
    return s.equalSubstring(l1, l2, l3)


def main():
    inp1 = "abcd"
    inp2 = "acde"
    inp3 = 0

    print(solution(inp1, inp2, inp3))


if __name__ == '__main__':
    main()
