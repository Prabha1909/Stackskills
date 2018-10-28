my_dict = {"Prabha":"19091990", "Saira": "29072000", "Sachin": "06052018"}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_son = my_dict.popitem()
print(my_son)
print(type(my_son))
print(type(my_dict.keys()))

#more operations using dictionary

print(my_dict.pop("Saira"))
my_dict["Saira"] = "29072000"
print(my_dict)
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(dict(zip(a,b)))
