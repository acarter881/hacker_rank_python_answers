import operator

def person_lister(f):
    def inner(people): # people is a list of lists
        # complete the function
        people = [[item1, item2, int(item3), item4] for item1, item2, item3, item4 in people] # Change the age from a string to an int
        
        people.sort(key=operator.itemgetter(2)) # Sort by age, ascending
        
        return [f(person) for person in people]
    
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
