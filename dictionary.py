Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"pooja","year":2026,"month":7}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 7}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['pooja', 2026, 7])
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 7)])
a={"year":2026,"month":"july","date":14}
a.update({"time":2})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
a.update({"time":2},{"day":"tue"})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({"time":2},{"day":"tue"})
TypeError: update expected at most 1 argument, got 2
a.update({"time":2,"day":"tue"})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'tue'}
a={"name":"lohitha","city":"vja"}
a.setdefault("mailid","lohitha123@gmail.com")
'lohitha123@gmail.com'
a
{'name': 'lohitha', 'city': 'vja', 'mailid': 'lohitha123@gmail.com'}
b={"name","lohitha","city","vij"}
b.setdefault("mailid","lohitha@gmail.com")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.setdefault("mailid","lohitha@gmail.com")
AttributeError: 'set' object has no attribute 'setdefault'
a={"state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("country")
'india'
a
{'state': 'ap'}
a.popitem()
('state', 'ap')
a
{}
a={"colour":"black","food":"biryani"}
a.copy()
{'colour': 'black', 'food': 'biryani'}
b=a.copy()
b
{'colour': 'black', 'food': 'biryani'}
len(a)
2
len(b)
2
a={"name":"pooja","city":"vja","name":"Lohitha"}
print(a)
{'name': 'Lohitha', 'city': 'vja'}
a={"name1":"lohitha","city":"vij","name2":"pooja"}
a
{'name1': 'lohitha', 'city': 'vij', 'name2': 'pooja'}
print(a)
{'name1': 'lohitha', 'city': 'vij', 'name2': 'pooja'}
a.count()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.index()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.index()
AttributeError: 'dict' object has no attribute 'index'
a.clear()
a
{}
a.update({"name":"lohitha"})
b
{'colour': 'black', 'food': 'biryani'}
a
{'name': 'lohitha'}

#single variable in multiple keys

a={"idnos":[10,20,30],"names":["lohitha","janu","brami"],"marks":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'names': ['lohitha', 'janu', 'brami'], 'marks': [60, 70, 80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['lohitha', 'janu', 'brami']), ('marks', [60, 70, 80])])
a.values()
dict_values([[10, 20, 30], ['lohitha', 'janu', 'brami'], [60, 70, 80]])

#task
a=[9,1,5,2,8,4,6,3,7,0]
b=[7,6,4,3,0,9,8,5,2,1]
a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a=[9,1,5,2,8,4,6,3,7,0]
>>> a.reverse()
>>> a
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> print(a)
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
>>> type(a)
<class 'list'>
>>> a.index(8)
4
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
