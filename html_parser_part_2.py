from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        dl = len(data.split('\n'))
        
        if dl == 1: word = 'Single-line Comment'
        else: word = 'Multi-line Comment'
        
        if data != '\n': print(f'>>> {word}\n{data}')
    
    def handle_data(self, data):
        if data != '\n': print(f'>>> Data\n{data}') 
  
html = ""    
   
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
