def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"