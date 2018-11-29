# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 1
a = a+1
print(a)
b = 'hello'
print(b)
c = b.title()
print(b)
print(c)
d = 'hello'
e = d.title()
print(d)
print(e)
name = 'Dave'
f = 'Hello! {0}!'.format(name)
print(f)
name = 'Loren'
f = 'Hello! {0}!'.format(name)
print(f)


age = 5
age = 'almost there'
age = 29.5
age = 'i really don\'t know' 
print(age)

print(type(2))

print('hello' + 'world')
print('Joke \n' * 3)
#print("Chen" + 3) Error because you can't put int and str together in concat. convert int to string.potential fixes below. 
print("Chen3")
print("Chen" + "3")
print("Chen" + str(3))
print('hello'.upper())
print()
print('GOODBYE'.lower())
print('\n')
print('the lord of the rings'.title())
print()

S1 = 'hello' + 'world'
S2 = 'Joke '*3
S3 = 5
result = S1 + S2*10
print(result)
print()

s1 = '4'
s2 = 6
s3 = 8
result2 = int(s1) + s2 + s3
print(result2)
print()

strExample = 'a,b-b,d,happy'
print(strExample)
splitStrExample = strExample.split()
print(splitStrExample)


age = 'fun'
like = 5

me = 'I am {} and I like {}'.format(age,like)
print(me)
age = 6.5
me = 'I am {} and I like {}'.format(age,like)
print(me)
