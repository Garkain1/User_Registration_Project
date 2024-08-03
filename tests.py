from main import process_user_registration


def test_valid_registration():
    valid_json = """
    {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "Broadway",
            "house_number": 1
        }
    }
    """
    result = process_user_registration(valid_json)
    print("Valid Registration Test:\n", result)


def test_invalid_age_registration():
    invalid_age_json = """
    {
        "name": "Bob",
        "age": 17,
        "email": "bob@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "Broadway",
            "house_number": 1
        }
    }
    """
    result = process_user_registration(invalid_age_json)
    print("Invalid Age Registration Test:\n", result)


def test_invalid_name_registration():
    invalid_name_json = """
    {
        "name": "Alice123",
        "age": 25,
        "email": "alice@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "Broadway",
            "house_number": 1
        }
    }
    """
    result = process_user_registration(invalid_name_json)
    print("Invalid Name Registration Test:\n", result)


def test_invalid_email_registration():
    invalid_email_json = """
    {
        "name": "Alice",
        "age": 25,
        "email": "alice@example",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "Broadway",
            "house_number": 1
        }
    }
    """
    result = process_user_registration(invalid_email_json)
    print("Invalid Email Registration Test:\n", result)


def test_invalid_city_registration():
    invalid_city_json = """
    {
        "name": "Alice",
        "age": 25,
        "email": "alice@example.com",
        "is_employed": true,
        "address": {
            "city": "N",
            "street": "Broadway",
            "house_number": 1
        }
    }
    """
    result = process_user_registration(invalid_city_json)
    print("Invalid City Registration Test:\n", result)


if __name__ == "__main__":
    test_valid_registration()
    test_invalid_age_registration()
    test_invalid_name_registration()
    test_invalid_email_registration()
    test_invalid_city_registration()
