import sys


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if k == 0:
            return False
        buffer = set()
        for i in range(len(nums)):
            x = nums[i]
            if x in buffer:
                return True
            if len(buffer) < k:
                buffer.add(x)
            else:
                buffer.remove(nums[i - k])
                buffer.add(x)

        return False


def solution(l1, l2):
    s = Solution()
    return s.containsNearbyDuplicate(l1, l2)


def main():

    inp1 = [1, 2, 3, 1]
    inp2 = 3
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
