try:
    height = float(input("height: "))
    weight = float(input("weight: "))
    BMI = weight / (height ** 2)
except ValueError:
    print("VE")
except:
    print("EEEEE")
else:
    print("Your BMI is", BMI)
finally:
    print("over")