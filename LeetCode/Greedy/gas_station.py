class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        so_far = []
        for i in range(len(gas)):
            cur = gas[i] - cost[i]
            so_far.append(cur)

        result = -1
        total = sum(so_far)
        if total < 0:
            return -1
        t = 0
        for c in range(len(so_far)):
            val = so_far[c]
            t += val

            if t < 0:
                result = -1
                t = 0
                continue
            if val >= 0 and result < 0:
                result = c

        return result


def solution(l1, l2):
    s = Solution()
    return s.canCompleteCircuit(l1, l2)


def main():
    inp1 = [1, 2, 3, 4, 5, 4, 5, 2, 4, 3, 6, 2]
    inp2 = [3, 4, 5, 1, 2, 3, 1, 3, 5, 6, 2, 0]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
