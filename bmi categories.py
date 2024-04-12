height = float(input("Please enter your height: "))
weight = int(input("Please enter your weight: "))
bmi_calculate = weight / height ** 2
if bmi_calculate < 18.5:
  print(f"Your BMI is {bmi_calculate} , you are underweight.")
elif bmi_calculate >=18.5 and bmi_calculate < 25:
  print(f"Your BMI is {bmi_calculate}, you have a normal weight.")
elif bmi_calculate >=25 and bmi_calculate < 30:
  print(f"Your BMI is {bmi_calculate}, you are slightly overweight.")
elif bmi_calculate >=30 and bmi_calculate < 35:
  print(f"Your BMI is {bmi_calculate}, you are obese.")
else:
  print(f"Your BMI is {bmi_calculate}, you are clinically obese.")