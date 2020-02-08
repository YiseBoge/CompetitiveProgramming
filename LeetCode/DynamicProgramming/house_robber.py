class Solution:
    def rob(self, nums: list) -> int:
        robberies = {}
        self.do_robbery(nums, 0, robberies)
        self.do_robbery(nums, 1, robberies)
        return max(robberies[0], robberies[1])

    def do_robbery(self, nums, current, robberies):
        if current in robberies:
            return robberies[current]

        if current == len(nums) - 1:
            robberies[current] = nums[current]
            return nums[current]
        if current > len(nums) - 1:
            robberies[current] = 0
            return 0

        result = None
        for i in range(2, 4):
            new = current + i
            new_res = self.do_robbery(nums, new, robberies)
            result = new_res if not result else max(result, new_res)

        result += nums[current]
        robberies[current] = result
        return result


def solution(l1):
    s = Solution()
    return s.rob(l1)


def main():
    inp1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(solution(inp1))


if __name__ == '__main__':
    main()
