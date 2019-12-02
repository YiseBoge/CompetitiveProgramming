import time


def main():
    t = time.time()
    i = 0
    while True:
        if i % 10000 == 0:
            if (time.time() - t) > 1:
                break
        i += 1
    print(i)


if __name__ == '__main__':
    main()
