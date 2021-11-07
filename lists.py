if __name__ == '__main__':
    N = int(input())
    z = list()
    
    for i in range(N):
        data = input().split()
        method = data[0] # insert, print, remove, append, sort, pop, reverse
        
        if method == 'insert':
            z.insert(int(data[1]), int(data[2]))
        elif method == 'print':
            print(z)
        elif method == 'remove':
            z.remove(int(data[1]))
        elif method == 'append':
            z.append(int(data[1]))
        elif method == 'sort':
            z.sort()
        elif method == 'pop':
            z.pop()
        elif method == 'reverse':
            z.reverse()
