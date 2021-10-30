def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1, 1):
        width = len(bin(number)[2:])
        
        print(str(i).rjust(width, ' '), 
              oct(i)[2:].rjust(width, ' '), 
              hex(i)[2:].rjust(width, ' ').upper(), 
              bin(i)[2:].rjust(width, ' '), 
              sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
