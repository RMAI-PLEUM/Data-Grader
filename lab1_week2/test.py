import decimal

# s = str(decimal.Decimal('1500.00000000000'))
# print (s.rstrip('0').rstrip('.') if '.' in s else s)

# i = 5000.3480002
# print( float(str(i)[:-1].rstrip('0')) if str(i)[-2] == '0' and str(i)[-3] == '0' else i)

a = 'a'
print(type(ord(a)))
print(chr(61))

s= "washbi"
a = []
for i in s:
    a.append(i)
print(a)