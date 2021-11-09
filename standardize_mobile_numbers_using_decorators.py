import re

my_re = re.compile(r'^(?:\+91|91|0)?(\d{10})$')

def wrapper(f):
    def fun(l): # l = ['07895462130', '919875641230', '9195969878']
        # complete the function
        f_l = list()
        
        for item in l:
            match = re.search(pattern=my_re, string=item).group(1)
            output = '+91' + ' ' + match[0:5] + ' ' + match[5:]
            f_l.append(output)
            
        return f(f_l)
    
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
