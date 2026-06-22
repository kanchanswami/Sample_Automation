
a = [10, 20, 30, 40, 50]
b = [10, 20, 30, 40, 50]
print(a is b)
print (id(a), id(b))

x =10 
y =10
print(x is y)
print(id(x), id(y))
print('P' in 'pune')
print(1 not in [10,20,30,40])

l1 = [1,2,3,4,5,100,200, -1, 0]

print(min(l1))
print(max(l1))
print(sum(l1))

student = (10,5,7,18,20)
print(list(enumerate(student)))

student_list = 'punemumbai'
print(list(enumerate(student_list)))

student_list = 'punemumbai'
for i in range (len(student_list)):
    print(i, student_list[i])



student_list = 'punemumbai'
for i in range (len(student_list)):
    print(i, student_list[i], i-len(student_list))


l1 = [1,2]
l2 = [10, 20]
l3 = l1 + l2
#print(l3)

l1.extend(l2)
print(l1)
print(l2)

for i in range(1, 6):
    print(i)
print(i)


i=10

while i>=1:
    print(i)
    i=i-1

for i in range(1,6):
    pass
print(i)

for i in range (1,10):
    if i==5:
        break
    print(i)

for i in range(1,10):
    if i==5 or i==7 or i==9:
        continue
    print(i)

mydict = { "One": 100, "Two": 200, "Three":300}

for i, j in mydict.items():
    print(i,j)
