def max(inp):
    if len(inp) == 1:
        return inp[0]

    if inp[0] > inp[1]:
        inp[1] = inp[0]
    return max(inp[1:])


inp = input('Enter Input : ').split()
inp = list(map(int, inp))
print(f'Max : {max(inp)}')