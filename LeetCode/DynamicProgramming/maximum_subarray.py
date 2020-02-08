class Solution:
    def maxSubArray(self, nums: list) -> int:
        result = nums[0]
        res = 0

        for i in nums:
            res += i
            if res > result:
                result = res
            if res < 0:
                res = 0

        return result


def solution(l1):
    s = Solution()
    return s.maxSubArray(l1)


def main():
    inp1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(solution(inp1))


if __name__ == '__main__':
    main()
