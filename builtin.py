
# len() used for string, list, dict, tuple
name = "sachin"
print(len(name)) #6

l = [1,2,3,4,5]
print(len(l)) #5

d = {"a":2,"b":3}
print(len(d)) #2

# range()
for i in range(2,10,2):
    print(i)

# enumerate()
# returns both index and value while looping
#1
fruits = ["apple","banana","mango"]

i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1


#2
fruits = ["apple","banana","mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


#3
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)


# zip()
names = ["Sachin","Rahul","Barsha"]
marks = [90,80,100]

for name,mark in zip(names,marks):
    print(name,mark)
