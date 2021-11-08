import re

email_regEx = re.compile(r'^[\w\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')

def fun(s):
    # return True if s is a valid email, else return False
    if re.search(pattern=email_regEx, string=s):
        return True
    else:
        return False
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
