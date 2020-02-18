class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        lengths = {}
        result = 0

        for i in range(len(nums)):
            self.do_dfs(i, nums, lengths)
            result = max(result, lengths[i])

        return result

    def do_dfs(self, current, nums, lengths):
        if current in lengths:
            return lengths[current]

        result = 0

        for i in range(current + 1, len(nums)):
            if nums[current] < nums[i]:
                result = max(result, self.do_dfs(i, nums, lengths))

        result += 1
        lengths[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.lengthOfLIS(l1)


def main():
    inp1 = [10, 9, 2, 5, 3, 7, 101, 18]

    print(solution(inp1))


if __name__ == '__main__':
    main()
