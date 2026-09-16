Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatypes
a=3
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''python'''
>>> type(e)
<class 'str'>
>>> f=5+9j
>>> type(f)
<class 'complex'>
>>> g=3j+7
>>> type(g)
<class 'complex'>
>>> i=6j
>>> type(i)
<class 'complex'>
>>> k=5+8i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
b=False
type(b)
<class 'bool'>
c=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
c="true"
type(c)
<class 'str'>
