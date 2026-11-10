height = 1.83
weight = 90
name = "Michal"
category = None

bmi = weight / (height**2)

if bmi < 18.5:
  category = "Malnutrition"
elif  18.5 <= bmi and bmi < 24.9:
  category = "Healthy weight"
elif  25 <= bmi and bmi < 29.9:
  category = "Slightly overweight"
elif  30 <= bmi and bmi < 39.9:
  category = "Obesity"
elif bmi <= 40: 
  category = "Severe obesity"
print ("Name:", name, ", Category:", category)

