def shift_chairs(chairs, n):
    before_stack, after_stack = [-float("inf")], [float("inf")]
    for i in range(n - 1, -1, -1):
        if not chairs[i]:
            after_stack.append(i)
    visited, result = set(), 0
    for i in range(n):
        if after_stack[-1] <= i:
            after_stack.pop()
        if not chairs[i]:
            if i not in visited:
                before_stack.append(i)
            continue
        if i - before_stack[-1] <= after_stack[-1] - i:
            result += i - before_stack.pop()
        else:
            temp = after_stack.pop()
            result += temp - i
            visited.add(temp)
    return result


if __name__ == "__main__":
    inp = int(input())
    inputs = list(map(int, input().split()))
    print(shift_chairs(inputs, inp))
