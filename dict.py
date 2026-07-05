d = {"a":1,"b":2,"c":3}
print(d.keys())#dict_keys(['a', 'b', 'c'])
print(d.values())#dict_values([1, 2, 3])
print(d.items())#dict_items([('a', 1), ('b', 2), ('c', 3)])
print(d.get("a"))#1
d.update({"d":4})#{'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)
d.pop("a")#{'b': 2, 'c': 3, 'd': 4}
print(d)
d.popitem()#{'b': 2, 'c': 3}
print(d)
d.clear()#{}
print(d)


e = d.copy()
print(e)

d.setdefault("d",0) #changes the value
print(d)





