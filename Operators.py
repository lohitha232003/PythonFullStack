Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic
a=5
b=3
print(a+b)
8
print(a-b)
2
print(a*b)
15
print(a**b)
125
print(a/b)#float value
1.6666666666666667
print(a//b)#int value
1
print(a%b)
2


#Assignment operator
a=3
b=5
a+=b

b+=a
b
13
b-=a
b
5
b*=a
b
40
b/=a
b
5.0
b//=a
b
0.0
b%=a
b
0.0



#comparision/Rational operator
a=6
b=8
a<b
True
b>a
True
a<=b
True
b>=a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a=5
b=5
a==b
True


#logical operator
a=4
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a!=b or a==b
True
not True
False
not False
True


#identify operator
a=8
type(a) is int
True
type(a) is not int
False
type(a) is float
False
type(a) is string
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    type(a) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(a) is str
False
type(a) is complex
False
type(a) is bool
False
b=5.0
type(b)is int
False
type(b) is float
True
type(b) is not str
True
c='Lohitha'
type(c) is not int
True
type(c)is str
True
type(c) is bool
False
d=True
type(d) is int
False
type(d) is float
False
type(d) is str
False
type(d) is bool
True


#Membership operator
a=2,3,4,5,6,7,8,9
9 in a
True
11 in a
False
7 in a
True
20 not in a
True
20 in a
False
3,6 in a
(3, True)
>>> 
>>> 
>>> #Bitwise operator
>>> 
>>> a=5
>>> b=7
>>> a&b
5
>>> a=7
>>> -(a+1)
-8
>>> b=-4
>>> ~b
3
>>> a=6
>>> b=7
>>> a^b
1
>>> a=8
>>> b=10
>>> a^b
2
>>> a=4
>>> a<<
SyntaxError: invalid syntax
>>> a=4
>>> a<<2
16
>>> b=6>>3
>>> b>>3
0
