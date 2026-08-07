def car_info(maker, model_number, **car_info):
    car_info["maker"] = maker
    car_info["model"] = model_number
    return car_info
car_info = car_info("Benz", "C260", clore="Blue", tow_package=True)
print(car_info)