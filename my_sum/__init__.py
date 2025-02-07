def sum(arg):
    """
    Calculate the sum of a list of numbers.

    Args:
        arg (list): A list of numerical values to be summed.

    Returns:
        int or float: The sum of the numerical values in the list.
    """
    total = 0
    for val in arg:
        total += val
    return total
