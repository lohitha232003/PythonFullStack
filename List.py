Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a=[2,4.5,"lohitha",6+9j,True,False]
>>> print(a)
[2, 4.5, 'lohitha', (6+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=8.8
>>> type(b)
<class 'float'>
>>> b=[8.9]
>>> type(b)
<class 'list'>
>>> 
>>> #append()
>>> a=["python","c","c++"]
>>> a.append("java")
>>> a
['python', 'c', 'c++', 'java']
>>> a.append("HTML","css")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("HTML","css")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["html","css"])
>>> a
['python', 'c', 'c++', 'java', ['html', 'css']]
>>> 
>>> #extend
>>> a=["html","css","js"]
>>> a.extend(["python","java"])
a
['html', 'css', 'js', 'python', 'java']

#insert
b=["via","hyd","vzg"]
b.insert(1,"chennai")
b
['via', 'chennai', 'hyd', 'vzg']

#index()
a=["python","java","c","js"]
a.index("c")
2
a.copy()
['python', 'java', 'c', 'js']
b=a.copy()
b
['python', 'java', 'c', 'js']
a.count("java")
1
a.count("python")
1
len(a)
4
d="lohitha"
len(d)
7


#sort()
a=["mango","apple","kiwi","berry"]
a.sort()
a
['apple', 'berry', 'kiwi', 'mango']
b=[4,6,2,9,6,7,8,2,]
b.sort()
b
[2, 2, 4, 6, 6, 7, 8, 9]

#reverse()
a=["ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds']
b=[5,7,2,8,0]
b.reverse()
b
[0, 8, 2, 7, 5]

#pop()
a=["black","white","red","blue","pink"]
a.pop()
'pink'
a.pop("white")
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
#in pop() we should give only position numbers
a.pop(1)
'white'
a
['black', 'red', 'blue']
a.remove("black")
a
['red', 'blue']
a.remove()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
a=["ap","ts","ka"]
a.clear()
a
[]
a.append()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.append()
TypeError: list.append() takes exactly one argument (0 given)
a.append("ap","ts","ka")
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.append("ap","ts","ka")
TypeError: list.append() takes exactly one argument (3 given)
a.append("lohitha")
a
['lohitha']
a.extend("geethika")
a
['lohitha', 'g', 'e', 'e', 't', 'h', 'i', 'k', 'a']
a.extend(["geethika"])
a
['lohitha', 'g', 'e', 'e', 't', 'h', 'i', 'k', 'a', 'geethika']

#Tuple()
a=(4,6.7,"python",7+9j,True,False)
print(a)
(4, 6.7, 'python', (7+9j), True, False)
type(a)
<class 'tuple'>
a.index(True)
4
a.count("python")
1
len(a)
6
