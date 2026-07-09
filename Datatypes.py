Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=5
type(a)
<class 'int'>
b=8.5
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
a="Lohitha"
type(a)
<class 'str'>
d='''Python'''
type(d)
<class 'str'>
x=5+9j
type(x)
<class 'complex'>
y=3j+7
type(y)
<class 'complex'>
z=9j
type(z)
<class 'complex'>
u=6+8i
SyntaxError: invalid decimal literal
bool=True
type(bool)
<class 'bool'>
x=false
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x=false
NameError: name 'false' is not defined. Did you mean: 'False'?
x=False
type(x)
<class 'bool'>
l='''python'''
print(l)
python

#datatypes conversions
#int
int(4)
4
int(8.7)
8
int('print')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int('print')
ValueError: invalid literal for int() with base 10: 'print'
int(5+9j)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(5+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(678)
678
int(True)
1
int(False)
0
#float...
float(7)
7.0
float(9.0)
9.0
float("hello")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(5j+8)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(5j+8)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
float(4556)
4556.0
0
0

#String...
str(3)
'3'
str(7.0)
'7.0'
str('python')
'python'
str(5+8j)
'(5+8j)'
str(True)
'True'
str(False)
'False'
>>> 
>>> 
>>> #complex...
>>> complex(8)
(8+0j)
>>> complex(7.0)
(7+0j)
>>> complex("lohitha")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex("lohitha")
ValueError: complex() arg is a malformed string
>>> complex(5j+3)
(3+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> 
>>> #boolean...
>>> bool(8)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    bool(8)
TypeError: 'bool' object is not callable
>>> bool(8)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    bool(8)
TypeError: 'bool' object is not callable
