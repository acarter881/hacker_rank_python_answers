if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([
        [i, j, k] for i in [char for char in range(0, x + 1, 1)]
        for j in [char for char in range(0, y + 1, 1)]
        for k in [char for char in range(0, z + 1, 1)] 
        if (i + j + k) != n
        ])
