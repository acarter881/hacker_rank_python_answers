from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)   
    z = int(n / k)   
    
    for i in range(0, n, k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k]).keys()))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
