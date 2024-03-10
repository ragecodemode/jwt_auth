from pydantic import BaseModel, EmailStr, Field, validator, model_validator

import re
import phonenumbers


class User(BaseModel):
    name: str
    lastname: str
    username: str
    email: EmailStr
    phonenumber: Field(max_length=16)
    password_1: Field(min_length=8, max_length=16)
    password_2: Field(min_length=8, max_length=16)

    @validator('email')
    def validation_email(cls, value: str) -> str:
        if not value:
            raise ValueError('Email address cannot be empty')

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(pattern, value):
            raise ValueError('Email address not correct')

        return value

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'User':
        pw1 = self.password_1
        pw2 = self.password_2

        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')

        return self

    @validator('phonenumber')
    def phonenumber_validation(cls, value: str) -> str:
        try:
            input_number = phonenumbers.parse(value)
            if not phonenumbers.is_valid_number(input_number):
                raise ValueError('Invalid phone number')
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('Invalid phone number format')
        return value


class UserLogin(BaseModel):
    email: EmailStr
    phonenumber: Field(max_length=16, default=None)
    password: Field(min_length=8, max_length=16)
