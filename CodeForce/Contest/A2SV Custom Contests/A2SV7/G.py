from collections import defaultdict
from math import comb


def take_training(courses):
    topic_count, difficulty_count = defaultdict(int), defaultdict(int)
    for topic, difficulty in courses:
        topic_count[topic] += 1
        difficulty_count[difficulty] += 1

    bad = sum((difficulty_count[difficulty] - 1) * (topic_count[topic] - 1)
              for topic, difficulty in courses)
    return comb(len(courses), 3) - bad


if __name__ == "__main__":
    results = []
    for _ in range(int(input())):
        inputs = []
        for _ in range(int(input())):
            inputs.append(list(map(int, input().split())))
        results.append(take_training(inputs))
    print(*results, sep="\n")
