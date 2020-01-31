class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        occurrence_record = {}
        story_holder = set()
        for c in arr:
            if occurrence_record.get(c) is None:
                occurrence_record[c] = 1
            else:
                occurrence_record[c] += 1

        for i in occurrence_record.values():
            if i in story_holder:
                return False
            story_holder.add(i)

        return True


def solution(l1):
    s = Solution()
    return s.uniqueOccurrences(l1)


def main():
    inp1 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

    print(solution(inp1))


if __name__ == '__main__':
    main()
