address = ["address1", "address2", "address3", "address1", "address2"]
#append method
address.append("India")
print(address)
#remove method
address.remove("address2")
print(address)
#pop method
my_country = address.pop(-1)
print(my_country)
#copy method
copy_of_address = address.copy()
print(copy_of_address)
#count method
print(address.count("address1"))
#extend method
address.extend("Th")
print(address)
#index method