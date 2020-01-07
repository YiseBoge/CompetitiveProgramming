class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and self.pings[0] < t - 3000:
            self.pings.pop(0)
        return len(self.pings)


def main():
    # Your MyCircularDeque object will be instantiated and called as such:

    obj = RecentCounter()
    print(obj.ping(3))
    print(obj.ping(100))
    print(obj.ping(3003))
    print(obj.ping(3101))
    print(obj.ping(6000))


if __name__ == '__main__':
    main()
