def get_float_value(kwargs: dict, key):
    value = kwargs.get(key)
    if value is not None:
        return float(value)
    else:
        return value