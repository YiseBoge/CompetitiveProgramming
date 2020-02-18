from LeetCode.Tries.__trie_node__ import TrieNode


class Solution:
    def longestWord(self, words: list) -> str:
        start = TrieNode()
        sorted_words = sorted(words)
        result = ""
        for word in sorted_words:
            current = start
            valid = True
            for i in range(len(word)):
                c = word[i]
                ind = ord(c) - ord("a")
                if not current.children[ind]:
                    if i == len(word) - 1:
                        current.children[ind] = TrieNode()
                    else:
                        valid = False
                        break
                current = current.children[ind]
            current.is_end = True
            if valid and len(word) > len(result):
                result = word
        return result


def solution(l1):
    s = Solution()
    return s.longestWord(l1)


def main():
    inp1 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

    print(solution(inp1))


if __name__ == '__main__':
    main()
