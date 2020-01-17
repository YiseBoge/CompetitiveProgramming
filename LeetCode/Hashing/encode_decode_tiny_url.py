class Codec:
    def __init__(self):
        self.urls = {}

    # def parse_short(self, short):
    #     res = ""
    #     for i in short:
    #         res += str(ord(i) - 65)
    #     return int(res)

    def to_short(self, integer):
        res = ""
        string = str(integer)
        for i in range(len(string)):
            char = string[i]
            res += chr(65 + int(char) + i)
        return res

    def make_hash(self, string):
        start = 11
        for i in string:
            start += ord(i) ** 2
        return start

    def encode(self, longUrl: str) -> str:
        ind = self.make_hash(longUrl)
        res = self.to_short(ind)

        self.urls[res] = longUrl
        return "http://tinator.com/" + res

    def decode(self, shortUrl: str) -> str:
        short = shortUrl.split("/")[-1]
        return self.urls[short]


def main():
    codec = Codec()
    short = codec.encode("https://leetcode.com/problems/design-tinyurl")
    long = codec.decode(short)
    print("tiny:", short)
    print("long:", long)


if __name__ == '__main__':
    main()
