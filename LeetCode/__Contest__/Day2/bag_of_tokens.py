class Solution:
    def bagOfTokensScore(self, tokens: list, P: int) -> int:
        sorted_tokens = sorted(tokens)
        start = 0
        end = len(tokens) - 1
        max_points = 0
        points = 0

        while end >= start:
            if P >= sorted_tokens[start]:
                P -= sorted_tokens[start]
                points += 1
                start += 1
            elif points < 1:
                return max_points
            else:
                P += sorted_tokens[end]
                points -= 1
                end -= 1

            if points > max_points:
                max_points = points

        return max_points


def solution(l1, l2):
    s = Solution()
    return s.bagOfTokensScore(l1, l2)


def main():
    inp1 = [100, 200, 300, 400]
    inp2 = 200

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
