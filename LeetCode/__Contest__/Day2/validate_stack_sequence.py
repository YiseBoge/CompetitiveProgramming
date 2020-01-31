class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        pop_index = 0
        stack = []
        for item in pushed:
            stack.append(item)
            while pop_index < len(popped):
                if len(stack) <= 0 or popped[pop_index] != stack[-1]:
                    break
                stack.pop()
                pop_index += 1

        return pop_index == len(popped)


def solution(l1, l2):
    s = Solution()
    return s.validateStackSequences(l1, l2)


def main():
    inp1 = [1, 2, 3, 4, 5]
    inp2 = [4, 3, 5, 1, 2]

    print(solution(inp1, inp2))


if __name__ == '__main__':
    main()
