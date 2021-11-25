num_van, cus = input('Enter Input : ').split('/')
num_van = int(num_van)
cus = list(map(int, cus.split()))
van = 1
for i in range(len(cus)):
    if van > num_van:
        van = 1
    print(f'Customer {i+1} Booking Van {van} | {cus[i]} day(s)')
    van += 1