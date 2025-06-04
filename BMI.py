# Write code below 💖
mass = int(input("Enter ur mass(in kg): ",))
height = float(input("Enter ur height(in meter): "))
bmi = mass/height**2
print(bmi)
print(
"""BMI Category 	BMI Range
Underweight 	Below 18.5
Healthy 	18.5 – 24.9
Overweight 	25.0 – 29.9
Obesity 	30.0 or above""")