def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
     #TODO: remove 'pass' and implement functionality
    a = int(a)
    b = int(b)
    while a >= b:
        a-=b

    return a
print(modulus(128,15))