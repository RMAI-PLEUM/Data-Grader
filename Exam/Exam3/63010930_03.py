def reverse(inp):
    if len(inp) == 0:
        return inp
    else:
        return reverse(inp[1:]) +inp[0]


inp = input('Enter Input : ')
a = ''
for i in inp:

    if i == ' ' or i == '.' or i == '“' or i == '”' or i == '!' or i == ';' or i == ',' or i == '?' or i == '’':
        pass
    else:
        a += i.lower()
b = reverse(a)

if a == b:
    print(f'\'{inp}\' is palindrome')
else: 
    print(f'\'{inp}\' is not palindrome')
    

