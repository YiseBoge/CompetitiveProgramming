def make_keyboard(string):
    index = 0
    result = []
    visited = set()
    for val in string:
        if len(result) == 0:
            result.append(val)
            visited.add(val)
            continue

        # print(index, val)

        if val not in visited and index == len(result) - 1:
            result.append(val)
            visited.add(val)
            index += 1
        elif val not in visited and index == 0:
            result.insert(0, val)
            visited.add(val)
        elif val not in visited:
            return "NO", None
        else:
            left = index - 1
            right = index + 1
            if 0 <= left and result[left] == val:
                index = left
            elif right < len(result) and result[right] == val:
                index = right
            else:
                return "NO", None
    for i in range(26):
        lt = chr(ord("a") + i)
        if lt not in visited:
            result.append(lt)
    return "YES", "".join(result)


def solution(inp1):
    return make_keyboard(inp1)


def main():
    inp1 = input()
    length = int(inp1)

    for i in range(length):
        inp1 = input()
        result = solution(inp1)
        print(result[0])
        if result[1]:
            print(result[1])


if __name__ == "__main__":
    main()
