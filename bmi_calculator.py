def get_valid_input(prompt,maxval,minval):
    while True:
        try :
            value =float(input(prompt))
            if value>= minval and value<= maxval:
                return value
            else:
                print ("Please enter a valid value between ",minval,"and", maxval)
        except ValueError:
            print("INVALID INPUT ! PLEASE ENTER A VALID INPUT .")

def bmi_calculate(height,weight) :
    bmi = weight / (height * height)
    return round(bmi,2)

def bmi_classify(bmi) :
   if bmi <18.5:
       return "Underweight"
   elif 18.5 <= bmi <= 25 :
       return "Normal"
   elif 25 <= bmi <= 30 :
       return "Overweight"
   else :
       return "Obese"

print("="*35)
print("       BMI CALCULATOR")
print("="*35)
while True:

    height = get_valid_input("Enter your height ( in Meters) :" ,3.0, 0.5)
    weight = get_valid_input("Enter your weight(in Kg) :",300,10)

    bmi = bmi_calculate(height,weight)
    category = bmi_classify(bmi)


    print("\n"+"="*35)
    print("Your BMI : ",bmi)
    print("Your category : ",category)
    print("\n"+"="*35)
    choice = input("Again want to calculate your BMI ?").lower()
    if choice == "no":
        break
