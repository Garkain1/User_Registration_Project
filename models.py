from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class Address(BaseModel):
    city: str = Field(..., min_length=2, description="City must be at least 2 characters long")
    street: str = Field(..., min_length=3, description="Street must be at least 3 characters long")
    house_number: int = Field(..., gt=0, description="House number must be a positive integer")


class User(BaseModel):
    name: str = Field(..., min_length=2, description="Name must be at least 2 characters long and contain only letters")
    age: int = Field(..., ge=0, le=120, description="Age must be between 0 and 120")
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator('name')
    def name_must_be_letters(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value

    @model_validator(mode='after')
    def check_age_employment(cls, values: 'User'):
        if values.is_employed and (values.age < 18 or values.age > 65):
            raise ValueError('Employed users must be between 18 and 65 years old')
        return values

    class Config:
        validate_assignment = True
