

def main():
    inp = int(input())
    ans = "YES" if (inp != 2) and (inp % 2 == 0) else "NO"
    print(ans)

if __name__ == '__main__':
    main()