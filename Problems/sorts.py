import random
import sys
import time


def __shuffled_list(maximum):
    result_list = []
    for j in range(1, maximum + 1):
        result_list += [j]

    for i in range(0, maximum):
        r = random.randrange(maximum)
        val = result_list[i]
        result_list[i] = result_list[r]
        result_list[r] = val
    return result_list


def __merge(list1, list2):
    i1 = 0
    i2 = 0
    new_list = []

    while i1 < len(list1) or i2 < len(list2):
        if i1 >= len(list1):
            new_list += list2[i2:]
            break
        elif i2 >= len(list2):
            new_list += list1[i1:]
            break
        elif list2[i2] <= list1[i1]:
            new_list += [list2[i2]]
            i2 += 1
        elif list1[i1] <= list2[i2]:
            new_list += [list1[i1]]
            i1 += 1
    return new_list


def merge_sort(the_list):
    size = len(the_list)

    if size == 1:
        return the_list
    else:
        half = size // 2
        return __merge(merge_sort(the_list[0:half]), merge_sort(the_list[half:]))


def quick_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    index = unsorted.pop()
    list1 = []
    list2 = []
    for i in unsorted:
        if index > i:
            list1.append(i)
        elif index <= i:
            list2.append(i)
    return quick_sort(list1) + [index] + quick_sort(list2)


def insertion_sort(the_list):
    i = 1
    while i < len(the_list):
        if the_list[i] < the_list[i - 1]:
            item = the_list[i]
            the_list[i] = the_list[i - 1]
            the_list[i - 1] = item
            if i > 1:
                i -= 1
        else:
            i += 1
    return the_list


def selection_sort(the_list):
    length = len(the_list)
    for i in range(length):
        smallest_index = i
        for j in range(i + 1, length):
            if the_list[j] < the_list[smallest_index]:
                smallest_index = j

        item = the_list[smallest_index]
        the_list[smallest_index] = the_list[i]
        the_list[i] = item

    return the_list


def counting_sort(the_list):
    min_val = the_list[0]
    max_val = the_list[0]
    for i in the_list:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    final_list = []
    count_holder = {}
    for i in range(min_val, max_val + 1):
        count_holder[i] = 0

    for j in the_list:
        count_holder[j] += 1

    for k in count_holder.keys():
        if count_holder[k] > 0:
            final_list += [k] * count_holder[k]

    return final_list


def solution(unsorted):
    # return insertion_sort(unsorted)
    # return selection_sort(unsorted)
    # return merge_sort(unsorted)
    # return quick_sort(unsorted)
    return counting_sort(unsorted)


def main():
    maximum = 10000
    inp = __shuffled_list(maximum)

    t = time.time()
    sys.stdout.write(str(solution(inp)))
    print()
    print(time.time() - t)


if __name__ == '__main__':
    main()
