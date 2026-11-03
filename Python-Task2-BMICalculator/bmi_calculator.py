def get_number(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter numbers only.")

weight = get_number("Enter weight in kg: ")
height = get_number("Enter height in meters: ")

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi:.2f} ({category})")
