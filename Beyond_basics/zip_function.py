list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

for i, j in zip(list1,list2):
    print("{} equals {}".format(i, j))