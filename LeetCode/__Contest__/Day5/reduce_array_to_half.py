class Solution:
    def minSetSize(self, arr: list) -> int:
        count_array = {}

        for i in arr:
            if count_array.get(i):
                count_array[i] += 1
            else:
                count_array[i] = 1

        sorted_values = sorted(count_array.values(), reverse=True)

        result = 0
        count_sum = 0
        half = len(arr) // 2
        for v in sorted_values:
            if count_sum >= half:
                break
            result += 1
            count_sum += v

        return result


def solution(l1):
    s = Solution()
    return s.minSetSize(l1)


def main():
    inp1 = [6, 2, 4, 2]

    print(solution(inp1))


if __name__ == '__main__':
    main()
