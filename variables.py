Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 print(10+20)
 
SyntaxError: unexpected indent
print(10+20)
30
a=10
b=50
print(a+b)
60
a=10
print(a)
10
z=50
print(z)
50
X=40
print(X)
40
name = "Lohitha"
print(name)
Lohitha
Name="lohitha"
print(Name)
lohitha
#concatinate
city="vijayawada"
country="India"
print(city,country)
vijayawada India
#special chacters
@=50
SyntaxError: invalid syntax
& = 70
SyntaxError: invalid syntax
_ = 30
print(_)
30
_d=90
print(_d)
90
 f=40
 
SyntaxError: unexpected indent
#keywords and space
if = 60
SyntaxError: invalid syntax
firstname="lohitha"
lastname="chintha"
print(firstname+ " " +lastname)
lohitha chintha
first name = "lohitha"
SyntaxError: invalid syntax
first_name = "lohitha"
print(first_name)
lohitha
#single line with 2 quotes
a=5,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=8
print(a+b)
13
#for single varibles giving multiple data
a = 23456789
print(a)
23456789
b= 2,3,4,5,6,7,8,9
print(b)
(2, 3, 4, 5, 6, 7, 8, 9)
#unpack and pack
a,b,c = 2,3,4
print(a,b,c)
2 3 4
>>> a = 4,5,6,7,8,9
>>> print(a)
(4, 5, 6, 7, 8, 9)
>>> a,b,c=20
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c=20
TypeError: cannot unpack non-iterable int object
>>> #delete keyword
>>> a = 7
>>> print(a)
7
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> 
>>> #usecase
>>> fname = "Lohitha"
>>> lname = "chintha"
>>> print(fname+lname)
Lohithachintha
>>> print(fname+ lname)
Lohithachintha
>>> print(fname+ " " +lname)
Lohitha chintha
>>> print(fname,lname)
Lohitha chintha
>>> 30print(fname,lname)
SyntaxError: invalid decimal literal
>>> #casesenstive
>>> name = "Lohitha"
>>> print(name)
Lohitha
>>> NAME = "Lohitha"
>>> print(NAME)
Lohitha
>>> Name = "Lohitha"
>>> print(Name)
Lohitha
>>> NaMe = "Lohitha"
>>> print(NaMe)
Lohitha
