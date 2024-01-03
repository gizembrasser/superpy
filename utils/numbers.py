# Function that checks whether an integer or float is positive.
def is_positive_number(number, optional_number=None):
    # Check if the value is an integer or float greater than 0.
    number_is_positive = isinstance(number, (int, float)) and number > 0
    # Check if the optional_number is either None or a positive integer or float.
    optional_number_is_positive = optional_number is None or (isinstance(optional_number, (int, float)) and optional_number > 0)

    # Return True if both conditions are met.
    return number_is_positive and optional_number_is_positive