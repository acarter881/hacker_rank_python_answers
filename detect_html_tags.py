# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re
from html.parser import HTMLParser

data = sys.stdin.read().split('\n')[1:] # Contains the lines of HTML

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'{tag}')
        
        if attrs:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')
                
# Create the HTML in string format
HTML = ''
for line in data: HTML += '\n' + line

cleaned_HTML = re.subn(pattern=r'<!--.*-->', repl='', string=HTML)[0]

parser = MyHTMLParser()
parser.feed(cleaned_HTML)
