def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "this is a zero divisible error"

print(divide(1,0))