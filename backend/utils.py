def replace_none_values(input_dict):
    """
    Replace None values in the input dictionary with the string 'None'.
    
    Args:
        input_dict (dict): Input dictionary.
    
    Returns:
        dict: Dictionary with None values replaced with 'None'.
    """
    return {key: ('None' if value is None else value) for key, value in input_dict.items()}

def rename_key(d, old_key, new_key):
    """
    Rename a key in a dictionary.

    Args:
        d (dict): The dictionary to operate on.
        old_key (hashable): The key to rename.
        new_key (hashable): The new key name.

    Returns:
        dict: The modified dictionary.
    """
    if old_key in d:
        d[new_key] = d.pop(old_key)
    return d
