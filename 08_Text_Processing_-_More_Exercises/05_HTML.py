article_title = input()
article_content = input()

print(f'<h1>')
print(f'{article_title}')
print(f'</h1>')

print(f'<article>')
print(f'{article_content}')
print(f'</article>')

command = input()
while command != 'end of comments':
    print(f'<div>')
    print(f'{command}')
    print(f'</div>')

    command = input()

