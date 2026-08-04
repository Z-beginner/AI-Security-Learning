#try and except
try:
    ed = float(input("被除数"))
    ee = float(input("除数"))
    result = ed / ee
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Error")
else:
    print(result)
finally:
    print("Done")