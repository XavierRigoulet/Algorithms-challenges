if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        command, *args = input().split()
        args = [int(x) for x in args]
        if command == 'print':
            print(L)
        else:
            getattr(L, command)(*args)