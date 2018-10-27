#printing a string
print("Hello")
#printing the type of the string
print(type("Hello"))
#We can even print the length of the string using len function
print(len("Hello"))
#we can assign string to a variabel and print it
my_string = "Hello world"
print(my_string)
#we can concatenate the string
print("100" + "100")
#we can concatenate string with other object types
#print([1, 2] + "100") This produces an error hence commented it out
#we can index and slice the string
print(my_string[0]) # prints the first letter of the string
print(my_string[2:5]) #prints third letter till fifth excluding the sixth one
#we can also prin the string in reverse
print(my_string[::-1])
#We can also print alternate characters in a string
print(my_string[::2])