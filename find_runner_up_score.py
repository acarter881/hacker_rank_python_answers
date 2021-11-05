if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(sorted(list(set(sorted(arr))))[:-1]))
