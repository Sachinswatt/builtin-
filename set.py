s = {1,2,3,4,5}
s.add(6) #{1,2,3,4,5,6}
s.update([7,8])#{1,2,3,4,5,6,7,8}
s.remove(2)#{1,3,4,5,6,7,8}
s.discard(8)#{1,3,4,5,6,7}
s.pop()#{3,4,5,6,7}
s.clear()#{}
t = s.copy()
print(s)
print(t)



a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))#{1, 2, 3, 4, 5, 6}
print(a.intersection(b))#{3, 4}
print(a.difference(b))#{1, 2}
print(b.difference(a))#{5,6}
print(a.symmetric_difference(b))#{1, 2, 5, 6}
print(b.symmetric_difference(a))#{1, 2, 5, 6}



x = {1,2,3,4,5,6}
y = {3,4}
print(x.issubset(y))#False
print(y.issubset(x))#True
print(x.issuperset(y))#True


