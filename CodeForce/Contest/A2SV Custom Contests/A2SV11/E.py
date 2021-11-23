def find_good_topics(teacher_interest, student_interest, n):
    diff = [t - s for t, s in zip(teacher_interest, student_interest)]
    diff.sort()
    result = 0
    for i, num in enumerate(diff):
        start, end = i + 1, n - 1
        while start <= end:
            mid = (start + end) // 2
            if num + diff[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
        result += n - start
    return result


if __name__ == "__main__":
    inp = int(input())
    inputs1 = list(map(int, input().split()))
    inputs2 = list(map(int, input().split()))
    print(find_good_topics(inputs1, inputs2, inp))
