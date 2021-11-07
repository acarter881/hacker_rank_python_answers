# Enter your code here. Read input from STDIN. Print output to STDOUT
lines = int(input())

and_pat = ' && '
pipe_pat = ' || '

new_text = ''

for i in range(lines):
    string = input()
    
    for j in range(0, len(string), 1):
        try:
            if string[j:j+4] == and_pat:
                new_text += ' and '
            elif string[j:j+4] == pipe_pat:
                new_text += ' or '
            else:
                new_text += string[j]
        except Exception as e:
            pass
    
    new_text += '\n'

newer_text = ''    

for line in new_text.split('\n'):
    new = line.replace(' && ', ' ')
    newer = new.replace(' || ', ' ')
    newer_text += newer + '\n'

newer_text = newer_text.strip()

print(newer_text)
