import itertools

variables=['A','B','C']
colors=['red','blue','green']

all_assignments=itertools.product(colors,repeat=len(variables))#all possible combinations banata hai

def valid(i):
    A,B,C=i
    return (A!=B)and (C!=B) and (C!=A)

solutions=[]
for i in all_assignments:
    if valid(i):
        solutions.append(dict(zip(variables,i)))

print("\n\n\nValid colorings of the map: ")
for sol in solutions:
    print(sol)
