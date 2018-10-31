x = {"a":1, "b":2}
y = {"c":3}

#in python 2 we use below steps to merge two dict
z_python2 = dict(x, **y)
print(z_python2)

# in python 3 we use below command
z_python3 = {**x, **y}
print(z_python3)

