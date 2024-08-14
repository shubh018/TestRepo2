

def test_function():
    try:
        new_variable = "New Variable"
        if str(new_variable) != 'New Variable':
            raise Exception("Strings don't match")

    except Exception as e:
        raise Expection("Failed")