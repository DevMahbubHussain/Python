dic = {'fname': 'Mahbub', 'lname': 'Hussain'}
print(dic['fname'])

# empty dict
d = {}
d['A'] = 'Mahbub'
d["B"] = 'Hussain'
print(d)

# update dic
dd = {'a': 'Mahbub', 'b': 'hussain'}
print(dd.get('aa', 'Mamun'))

print(dd.pop('a'))
print(dd)
print(len(dd))

ddd = {'fname': 'Mahbub', 'lname': 'Hussain'}

dd.update(ddd)
print(dd)
# print(ddd.popitem())

# items
newdic = {'fname': 'Mahbub', 'lname': 'Hussain'}
for k, v in newdic.items():
    print(k, "====", v)

newdic2 = {'fname': 'Mahbub', 'lname': 'Hussain'}
for k in newdic2.keys():
    print(k)

newdic3 = {'fname': 'Mahbub', 'lname': 'Hussain'}
for v in newdic3.values():
    print(v)

# setdefault & copy method

#setdefault
setdata = {100:'Mahbub',200:'Hussain','300':'Mamun'}
setdata.setdefault(100,"MMMM")
print(setdata)
