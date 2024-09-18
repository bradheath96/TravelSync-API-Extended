def is_non_empty_string(value):
    return isinstance(value, str) and len(value) > 0

def is_valid_coordinates(value):
    return isinstance(value, dict) and "lat" in value and "lng" in value