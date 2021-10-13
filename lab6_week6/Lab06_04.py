material = [[int(x) for x in i.split(' ')] 
for i in input("Enter Input : ").split(',') ]

print(material)


# def calTaste(mix, sour_product, salt_sum):
#     if len(mix) == 0:
#         return abs(salt_sum-sour_product)

#     sour_product *= mix[0][0]
#     salt_sum += mix[0][1]

#     return calTaste(mix[1:], sour_product, salt_sum)

# def mix(material):
#     results = []
#     def go(mix, pos, n):
#         if n == len(material):
#             if len(mix) != 0:
#                 results.append(calTaste(mix, 1, 0))
#             return
        
#         mix1 = mix.copy()
#         mix1.append(material[pos])
#         go(mix1, pos+1, n+1)
#         mix2 = mix.copy()
#         go(mix2, pos+1, n+1)
    
#     go([], 0, 0)
#     return min(results)

# print(mix(material))