

def test_function():
    try:
        new_variable = "New Variable"
        if str(new_variable) != 'New Variable':
            raise Exception("Strings don't match")

    except Exception as e:
        raise Expection("Failed")

def test_function_2():
    try:
        new_variable = "New Varaible 2"
        if str(new_variable) != 'New Variable 2':
            raise Exception("Strings don't match")

    except Exception as e:
        raise Expection("Failed")