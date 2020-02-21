class Solution:
    def rob(self, nums: list) -> int:
        robberies0 = {}
        robberies1 = {}
        robberies2 = {}
        self.do_robbery(nums, 0, robberies0, 0)
        self.do_robbery(nums, 1, robberies1, 1)
        self.do_robbery(nums, 2, robberies2, 2)
        if len(nums) <= 3:
            return max(nums) if len(nums) > 0 else 0
        return max(robberies0[0], robberies1[1], robberies2[2])

    def do_robbery(self, nums, current, robberies, start):
        if current in robberies:
            return robberies[current]

        if current == len(nums) - 1 and start != 0:
            robberies[current] = nums[current]
            return nums[current]
        if current >= len(nums) - 1:
            return 0

        result = None
        for i in range(2, 4):
            new = current + i
            new_res = self.do_robbery(nums, new, robberies, start)
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
