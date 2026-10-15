from collections.abc import Iterable, Mapping
from numbers import Real
from typing import Any


def calculate_average(numbers: Iterable[float]) -> float:
    """Return the arithmetic mean of the given numbers.

    Raises:
        ValueError: If ``numbers`` is None, is a string, is not iterable,
            is empty, or contains non-numeric values (including bools).
    """
    if numbers is None:
        raise ValueError("Cannot calculate the average of None.")
    if isinstance(numbers, (str, bytes)):
        raise ValueError(
            f"Expected an iterable of numbers, got a string: {numbers!r}."
        )
    if not isinstance(numbers, Iterable):
        raise ValueError(
            "Expected an iterable of numbers, got "
            f"{type(numbers).__name__}."
        )
    values = list(numbers)
    if not values:
        raise ValueError("Cannot calculate the average of an empty sequence.")
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise ValueError(
                f"All values must be numeric; got {value!r} at index {index}."
            )
    return sum(values) / len(values)


def get_user_name(user: Mapping[str, Any]) -> str:
    """Return the user's name in upper case.

    Raises:
        ValueError: If ``user`` is None or not a mapping, has no ``"name"``
            key, or the name is not a non-empty string.
    """
    if user is None:
        raise ValueError("User record must not be None.")
    if not isinstance(user, Mapping):
        raise ValueError(
            f"User record must be a mapping, got {type(user).__name__}."
        )
    if "name" not in user:
        raise ValueError("User record is missing the required 'name' field.")
    name = user["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError(
            f"User 'name' must be a non-empty string, got {name!r}."
        )
    return name.upper()
