import math

# only gets it for odd numbers

# integer
x = 53

# primitive roots
roots = []
values_to_equal = [*range(1, x)]
for y in range(1,x):
    potential_roots = []
    for z in range(1,x):
        potential_roots.append((y**z) % x)
    potential_roots.sort()
    if(potential_roots == values_to_equal):
        roots.append(y)

print("Primitive Roots: " + str(roots))