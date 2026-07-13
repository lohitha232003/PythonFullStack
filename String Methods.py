Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()
a="Lohitha"
len(a)
7
b="Vijayawada"
len(b)
10
c=""
len(c)
0
d=" "
len(d)
1
e="i love vijayawada"
len(e)
17


#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("little")
1
a.count("t")
5
a.count("k")
2

 

#find a string find()
a="python"
a.find("h")
3
a.find(o)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.find(o)
NameError: name 'o' is not defined
a.find("o")
4
b="hello"
b.find("l")
2
b.find("L")
-1


#escape sequences
#\n - new line
#\t - tab Space
a="name\nmailid\tmobile number\ncollage\tbranch"
print(a)
name
mailid	mobile number
collage	branch
b="name:Lohitha\nmailid:lohitha@gmail.com\tPh No:9876543210\ncollage:Klu\tbranch:CS&IT"
print(b)
name:Lohitha
mailid:lohitha@gmail.com	Ph No:9876543210
collage:Klu	branch:CS&IT


#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b = "python java"
b.replace("p","c")
'cython java'
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'

#upper()
a="code"
a.upper()
'CODE'
#lower()
b="HELLO"
b.lower()
'hello'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
d="Lohitha"
d.capitalize()
'Lohitha'
a="lohitha"
a.isupper()
False
a.islower()
True
b="HELLO"
b.isupper()
True
b.islower()
False
a.isalpha()
True
b.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="12345"
d.isdigit()
True
e="1,2,3,4"
e.isdigit()
False
a="pooja1234"
a.isalnum()
True
b="lohitha@123"
a.isdigit()
False
b.isalnum()
False


f="python course"
f.startswith("d")
False
f.startswith("p")
True
f.endswith("e")
True

#strip()
#lstrip(),rstrip()
a=("     lohitha     ")
a.strip()
'lohitha'
a.lstrip()
'lohitha     '
a.rstrip()
'     lohitha'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="my name is lohitha"
b.split()
['my', 'name', 'is', 'lohitha']

#join()
a="html","css","java","python"
"".join(b)
'my name is lohitha'
"".join(a)
'htmlcssjavapython'
" ".join(a)
'html css java python'
c="lohitha"
" ".join(c)
'l o h i t h a'

#concatenation()
fname="lohitha"
lname="chintha"
print(fname+lname)
lohithachintha
print(fname+" "+lname)
lohitha chintha
print(fname.title()+" "+lname.title())
Lohitha Chintha
#or
print((fname+" "+lname).title())
Lohitha Chintha

#formatting()
a=5
b=7
print("the sum is",a+b)
the sum is 12
c="lohitha"
d="chintha"
print("My name is",c+d)
My name is lohithachintha
print("my name is",c+" "+d)
my name is lohitha chintha

#format()
a="lohi"
>>> b="janu"
>>> print("hello {}{}".format(a,b))
hello lohijanu
>>> print("hello {} {}".format(a,b))
hello lohi janu
>>> print("hello {} hello {}".format(a,b))
hello lohi hello janu
>>> print("hello {}\nhello {}".format(a,b))
hello lohi
hello janu
>>> print("hello { }{ }".format(a,b))
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    print("hello { }{ }".format(a,b))
KeyError: ' '
>>> 
>>> #fstring()
>>> a="sitha"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitharam
>>> print(f"hello {a} {b}")
hello sitha ram
>>> print(f"hello {a} hello {b}")
hello sitha hello ram
>>> print(f"hello {a}\nhello{b}")
hello sitha
helloram
>>> print(f"hello {a}\nhello {b}")
hello sitha
hello ram
