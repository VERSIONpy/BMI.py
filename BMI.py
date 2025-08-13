# Write code below 💖
mass = int(input("Enter ur mass(in kg): ",))
height = float(input("Enter ur height(in cm): "))
A = height / 100  # Convert height from cm to meters
bmi = mass/A**2
print(bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Healthy")
elif 25 <= bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("obesity")
    print("You are a lazy person")
else:
    print("Invalid input")
print("Have a great day!") 
