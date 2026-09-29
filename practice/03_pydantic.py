"""
Part 3 — Pydantic v2
=====================
Based on https://docs.pydantic.dev — note this is Pydantic v2 (the Rust-
core rewrite). If any tutorial you find online uses `@validator` or
`.dict()`, that's v1 syntax — deprecated. Use `@field_validator` and
`.model_dump()` instead, as below.

Requires: pydantic  (uv add pydantic   OR   pip install pydantic)

Why this matters: LangChain tool schemas and LangGraph state objects are
commonly just Pydantic BaseModels — this is the actual mechanism behind
"structured output" in both frameworks.
"""

from typing import Optional

from pydantic import BaseModel, Field, ValidationError, field_validator


# ---------------------------------------------------------------------------
# Exercise 12 — Basic BaseModel + read a ValidationError
# ---------------------------------------------------------------------------
# Define a `User` model with:
#   id: int
#   name: str
#   email: Optional[str] = None   (defaults to None if not provided)
#
# TODO: define the class below

class User(BaseModel):
    # TODO: id: int
    # TODO: name: str
    # TODO: email: Optional[str] = None
    pass


def exercise_12():
    # This should succeed:
    user = User(id=1, name="Joshua")
    print(user)

    # TODO: this should FAIL — pass id="not-an-int" and catch the
    # ValidationError, then print e.errors() to see the structured
    # error detail Pydantic gives you (field, message, input value).
    try:
        raise NotImplementedError
    except ValidationError as e:
        print(e.errors())


# ---------------------------------------------------------------------------
# Exercise 13 — Field() constraints
# ---------------------------------------------------------------------------
# Define a `Product` model:
#   name: str, min_length=2
#   price: float, gt=0  (must be greater than zero)
#   description: str with a Field(description=...) metadata string
#
# Then deliberately violate EACH constraint once and print the error.

class Product(BaseModel):
    # TODO: name: str = Field(min_length=2)
    # TODO: price: float = Field(gt=0)
    # TODO: description: str = Field(description="Short product description")
    pass


def exercise_13():
    # TODO: try Product(name="A", price=10, description="ok") -> should fail (name too short)
    # TODO: try Product(name="Chair", price=-5, description="ok") -> should fail (price <= 0)
    # TODO: try Product(name="Chair", price=49.99, description="A chair") -> should succeed
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 14 — Custom validator with @field_validator (v2 syntax)
# ---------------------------------------------------------------------------
# Define a `SignUp` model with a `username: str` field. Add a
# @field_validator("username") classmethod that rejects usernames
# containing spaces (raise ValueError with a clear message).

class SignUp(BaseModel):
    username: str

    # TODO:
    # @field_validator("username")
    # @classmethod
    # def no_spaces(cls, value):
    #     if " " in value:
    #         raise ValueError("username must not contain spaces")
    #     return value


def exercise_14():
    # TODO: SignUp(username="joshua_dev") -> should succeed
    # TODO: SignUp(username="joshua dev") -> should raise ValidationError
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 15 — Nested models
# ---------------------------------------------------------------------------
# Define `Address` (street: str, city: str, country: str) and a `Customer`
# model that has `name: str` and `address: Address`. Instantiate Customer
# by passing a plain nested dict for `address` and confirm Pydantic
# validates it recursively into an actual Address instance.

class Address(BaseModel):
    # TODO: street, city, country — all str
    pass


class Customer(BaseModel):
    # TODO: name: str
    # TODO: address: Address
    pass


def exercise_15():
    data = {
        "name": "Joshua",
        "address": {"street": "1 Main St", "city": "Abuja", "country": "Nigeria"},
    }
    # TODO: customer = Customer(**data)
    # TODO: print(customer)
    # TODO: print(type(customer.address))  # should be <class '__main__.Address'>
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 16 — model_dump() and model_dump_json()
# ---------------------------------------------------------------------------
# Reuse the Customer model from exercise 15. Convert an instance to a
# plain dict with .model_dump(), and to a JSON string with
# .model_dump_json(indent=2). Note: these replaced .dict()/.json() in v1.

def exercise_16():
    customer = Customer(
        name="Joshua",
        address={"street": "1 Main St", "city": "Abuja", "country": "Nigeria"},
    )
    # TODO: as_dict = customer.model_dump()
    # TODO: as_json = customer.model_dump_json(indent=2)
    # TODO: print both, and print(type(as_dict)) / print(type(as_json))
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 17 — model_validate() on raw dict/JSON data
# ---------------------------------------------------------------------------
# Simulate data straight off an API response (a plain dict, no model
# involved yet). Parse it into your User model with User.model_validate().

def exercise_17():
    raw_api_response = {"id": 42, "name": "API User", "email": "a@example.com"}
    # TODO: user = User.model_validate(raw_api_response)
    # TODO: print(user)
    raise NotImplementedError


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n--- Exercise 12 ---")
    exercise_12()

    print("\n--- Exercise 13 ---")
    exercise_13()

    print("\n--- Exercise 14 ---")
    exercise_14()

    print("\n--- Exercise 15 ---")
    exercise_15()

    print("\n--- Exercise 16 ---")
    exercise_16()

    print("\n--- Exercise 17 ---")
    exercise_17()
