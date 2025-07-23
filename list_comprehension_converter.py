squre = []
#tradional loop
for i in range(10):
    squre.append(i*i)
evens = []
for i in range(10):
    if i%2==0:
        evens.append(i)

pairs=[]
for i in range(3):
    for j in range(2):
        pairs.append((i,j))

# comprehension
squre = [i*i for i in range(10)]
evens = [i for i in squre if i%2==0]
pairs = [(i,j) for i in range(3) for j in range(2)]


