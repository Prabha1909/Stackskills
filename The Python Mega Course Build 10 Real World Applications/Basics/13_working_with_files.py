# my_file = open("files/sample.txt")
# fruits = my_file.read()
# my_file.close()
# print(fruits)
# myfile = open("files/sample.txt")
# content = myfile.read()
# print(content)
# content = content.splitlines()   #returns a list
# print(content)

#we can use seek method to bring back the cursor position to 0


with open(r"C:\Users\pselvam\Desktop\avl.txt", 'r') as f: #using context manager
    for line in f:
        print(line)
