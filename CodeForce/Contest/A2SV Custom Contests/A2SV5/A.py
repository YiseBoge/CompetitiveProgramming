from collections import defaultdict


def find(comparisons):
    greater = defaultdict(set)
    smaller = defaultdict(set)
    for string in comparisons:
        comparer = '>' if '>' in string else '<'
        small, big = (string[0], string[-1]) if comparer == "<" else (string[-1], string[0])
        greater[small] |= {big} | greater[big]
        smaller[big] |= {small} | smaller[small]
    mid = ""
    for char in 'ABC':
        if greater[char].intersection(smaller[char]):
            return "Impossible"
        if greater[char] and smaller[char]:
            mid = char
    return smaller[mid].pop() + mid + greater[mid].pop()


if __name__ == "__main__":
    inputs = [input() for _ in range(3)]
    print(find(inputs))
