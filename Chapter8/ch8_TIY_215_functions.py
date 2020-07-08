def sandwich_order(*toppings):
    print(toppings)

def build_profile(first, last, **other_info):
    other_info['first'] = first
    other_info['last'] = last
    return other_info

def build_car(manufacturer, model, **other_info):
    other_info['manufacturer'] = manufacturer
    other_info['model'] = model
    return other_info