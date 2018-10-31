# if 1 > 0:
#     print("It is greater")
# else:
#     print("No, it is not greater")
#


pincode = {"Thangal":600019, "Tollgate": 600081, "Parrys": 600001}

pin = int(input("Enter the pincode: "))

if pin in pincode.values():
    print("Pincode found")
else:
    print("incorrect pin")
    print("This can only accessed by ")
    for keys in pincode.keys():
        print(keys)