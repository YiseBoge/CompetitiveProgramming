import sys


def relative_sort_array(arr1, arr2):
    final_list = []

    min_val = arr1[0]
    max_val = arr1[0]
    for i in arr1:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    count_holder = {}
    for i in range(min_val, max_val + 1):
        count_holder[i] = 0

    for j in arr1:
        count_holder[j] += 1

    for k in arr2:
        if count_holder[k] > 0:
            final_list += [k] * count_holder[k]
            count_holder[k] = 0

    for l in count_holder.keys():
        if count_holder[l] > 0:
            final_list += [l] * count_holder[l]

    return final_list


def solution(l1, l2):
    return relative_sort_array(l1, l2)


def main():
    # inp1 = sys.stdin.readline().split()
    # inp2 = sys.stdin.readline().split()
    inp1 = [1, 2, 2, 1]
    inp2 = [2, 2]
    sys.stdout.write(str(solution(inp1, inp2)))


if __name__ == '__main__':
    main()
