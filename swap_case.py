def swap_case(s):
    s2 = ''
    
    for letter in s:
        if letter.upper() == letter:
            s2 += letter.lower()
        else:
            s2 += letter.upper()
            
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
