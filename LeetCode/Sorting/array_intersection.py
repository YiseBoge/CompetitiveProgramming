import sys


def array_intersection(nums1, nums2):
    commons = {}
    result = []

    for i in nums1:
        commons[i] = 1

    for j in nums2:
        if j in commons.keys():
            commons[j] = 2

    for k in commons.keys():
        if commons[k] == 2:
            result += [k]

    return result


def solution(l1, l2):
    return array_intersection(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [1, 2, 2, 1]
    inp2 = [2, 2]
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
