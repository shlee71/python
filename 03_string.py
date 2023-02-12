#! /usr/bin/python3
print('Hello World')
print("Hello World")

print("'1'+'1'", '1'+'1')
print('hello world '*3)
print("len('Hello World'*100)",len('Hello World'*100))
print("'Hello World'.replace('world','universe')", 'Hello World'.replace('World','universe'))

#escape
print("Hell'o' \"World")
#newline
print("Hello\nWorld!!!")
#docstring
print('''
Hello
World
''')
print("""
Hello
World
""")
      
a = 'Hello Python'
print(a)
#length
print(len(a))
#index
print(a[0])
print(a[1])
#range of string <= <
print(a[0:1])
print(a[2:5])
print(a[-1])

print( (a+'\n')*2)
#positional formating
print('{} is {}'.format('My age',12))
print('{name} is {age} years old'.format(name='SHLEE',age=53))
