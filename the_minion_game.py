def minion_game(string):
    # your code goes here
    kevin_score, stuart_score = 0, 0
    
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    
    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print(f'Stuart {stuart_score}')

if __name__ == '__main__':
    s = input()
    minion_game(s)
