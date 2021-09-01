def weirdSubtract(n,k):
	i = 0
	
	while i<k:
		if n%10 == 0:
			n = n/10
			
		else :
			n-=1
		
		i+=1 
	return int(n)

n,s = input("Enter num and sub : ").split(" ")

print(weirdSubtract(int(n),int(s)))
print("update from github")
