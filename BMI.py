weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
  print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
  print("Your weight is normal (healthy weight).")
elif bmi >= 25 and bmi < 30:
  print("You are overweight.")
else:
  print("You are obese.")









   



