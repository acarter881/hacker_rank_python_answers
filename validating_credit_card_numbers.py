# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

cc_numbers = int(input())

my_regEx = re.compile(r'^[4-6]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$')

for i in range(cc_numbers):
    invalid = False
    
    cc_number = input()
    
    # Test that the hyphenated values are in pairs of 4
    if '-' in cc_number:
        test_thing = cc_number.split('-')
        
        if not all([z == 4 for z in [len(item) for item in test_thing]]):
            invalid = True  
    
    # Test that 4 numbers do not repeat themselves
    test_string = ''
    
    for thing in cc_number:
        if thing.isalnum():
            test_string += thing
            
    for i in range(len(test_string)):
        try:
            if test_string[i] == test_string[i+1] == test_string[i+2] == test_string[i+3]:
                invalid = True
        except Exception as e:
            pass
    
    # Print the results
    if invalid == True:
        print('Invalid')
    else:
        if re.search(pattern=my_regEx, string=cc_number):
            print('Valid')
        else:
            print('Invalid')
