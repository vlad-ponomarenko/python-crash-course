def make_car(manufacturer, model, **kvargs):
    kvargs["manufacturer"] = manufacturer
    kvargs["model"] = model
    return kvargs


my_car = make_car("audi", "tt", color="blue", tow_package=True)
print(my_car)
