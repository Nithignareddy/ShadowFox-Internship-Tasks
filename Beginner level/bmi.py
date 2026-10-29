height = 1.75
weight = 70
bmi = weight / (height*height)
print("BMI:", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("overweight")
    