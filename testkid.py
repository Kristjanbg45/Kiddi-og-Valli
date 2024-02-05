def how_many(lis1, lis2):
    # Base case: If either list is empty, there are no common elements
    if not lis1 or not lis2:
        return 0
    
    a = 0
    if lis1[0] in lis2:
        a += 1

    rest = how_many(lis1[1:], lis2)
    a += rest

    return a


# result1 = how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
# print(result1)  

# result2 = how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
# print(result2) 

# a = how_many['f', 'g', 't'],['a', 'b', 'c', 'd', 'e']
# print(a)  # 0

b = how_many(['a', 'b', 'c', 'd', 'e'], ['f', 'g', 't'])
print(b)  # Output: 0