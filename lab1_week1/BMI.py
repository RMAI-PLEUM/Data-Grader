def BMI(h,w):
    bmi = w/(h**2)

    if(bmi < 18.5):
        return "Less Weight"
    elif(bmi >= 18.5) and (bmi<23):
        return "Normal Weight"
    elif(bmi >= 23) and (bmi<25):
        return "More than Normal Weight"
    elif(bmi >= 25) and (bmi<30):
        return "Getting Fat"
    elif(bmi >= 30):
        return "Fat"
    
data = input("Enter your High and Weight : ").split(" ")
h, w = list(map(float,data))
print(BMI(h,w))

# test push to git

    



