from models import User
from pydantic import ValidationError

def process_user_registration(json_string: str) -> str:
    try:
        user = User.parse_raw(json_string)
        return user.json()
    except ValidationError as e:
        return str(e)

if __name__ == "__main__":
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
    print(process_user_registration(valid_json))
