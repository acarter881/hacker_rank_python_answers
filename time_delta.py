#!/bin/python3
import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff = abs(dt1-dt2)
    total_time = (diff.days * 86400) + diff.seconds
    
    return str(total_time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
