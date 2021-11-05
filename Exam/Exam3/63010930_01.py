def harmonic_sum(n):
    sum = 0
    n1 = 1
    def harmonic(n1 ,sum):
        if n1 == n:
            sum += 1/n1
            if n != 1:
                print(f'1/{n} = ',end='')
            if n == 1:
                print(f'{n1} = ',end='')
            return sum
            
        else:
            if n1 == 1:
                sum += 1
                print(f'{n1} + ',end='')
            elif n1 > 1:
                sum += 1/n1
                print(f'1/{n1} + ',end='')
            return harmonic(n1+1, sum)

    return harmonic(n1, sum)      
    
print(' *** Harmonic sum ***')
num = int(input("Enter number of terms : ")) 
print("%.8f" %(harmonic_sum(num)))
# print(harmonic_sum(num))



        
