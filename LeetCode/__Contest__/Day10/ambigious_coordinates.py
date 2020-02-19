class Solution:
    def ambiguousCoordinates(self, S: str) -> set:
        results = set()
        for i in range(2, len(S) - 1):
            lst1 = self.find_possibles(S[1:i])
            lst2 = self.find_possibles(S[i:len(S) - 1])
            for x in lst1:
                for y in lst2:
                    new_string = "(" + str(x) + ", " + str(y) + ")"
                    results.add(new_string)
        return results

    def find_possibles(self, string) -> set:
        results = set()
        if self.valid(string):
            results.add(string)
        for i in range(1, len(string)):
            new_string = string[:i] + "." + string[i:]
            if self.valid(new_string):
                results.add(new_string)
        return results

    def valid(self, string):
        try:
            x = int(string)
            if str(x) == string:
                return True
        except:
            if len(string) == 1:
                return True
            done_first = False
            zero_count = 0
            for i in string:
                if i != "0":
                    if not done_first:
                        if zero_count > 1 or zero_count == 1 and string[1] != ".":
                            return False
                        done_first = True
                    zero_count = 0
                else:
                    zero_count += 1

            return zero_count == 0


def solution(l1):
    s = Solution()
    return s.ambiguousCoordinates(l1)


def main():
    inp1 = "(0123)"

    print(solution(inp1))


if __name__ == '__main__':
    main()
