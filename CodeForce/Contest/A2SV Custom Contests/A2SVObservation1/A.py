def send_messages(dorms, queries):
    result = []
    prefix = ind = 0
    for i, rooms in enumerate(dorms):
        prefix += rooms
        while ind < len(queries) and queries[ind] <= prefix:
            result.append(f"{i + 1} {queries[ind] - prefix + rooms}")
            ind += 1
    return "\n".join(result)


if __name__ == "__main__":
    inp1, inp2 = list(map(int, input().split()))
    inputs1 = list(map(int, input().split()))
    inputs2 = list(map(int, input().split()))
    print(send_messages(inputs1, inputs2))
