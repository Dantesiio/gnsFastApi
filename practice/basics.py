"""Small Python snippets to refresh core programming concepts."""
from __future__ import annotations

from typing import Any

# Constants with clear names make the intent of the data obvious.
DEFAULT_USERNAMES: list[str] = ["mentor", "student", "observer"]


def describe_collections() -> dict[str, Any]:
    """Show different collection types and how to manipulate them."""
    # Lists keep order and can contain duplicates.
    cities = ["Bogota", "Medellin", "Cali"]
    cities.append("Cartagena")

    # Sets are great when you only care about unique values.
    unique_roles = {"leader", "facilitator", "note_taker"}
    unique_roles.add("presenter")

    # Dictionaries map keys to values for quick lookups.
    interview_plan = {
        "warm_up": "team introductions",
        "challenge": "design an API",
        "retro": "share lessons learned",
    }

    return {
        "cities": cities,
        "unique_roles": sorted(unique_roles),
        "interview_plan": interview_plan,
    }


def format_candidate_summary(name: str, strengths: list[str]) -> str:
    """Build a readable string using f-strings."""
    formatted_strengths = ", ".join(strengths)
    return f"Candidate {name.title()} shines in: {formatted_strengths}."


def count_even_numbers(values: list[int]) -> int:
    """Count even numbers to practice loops, conditionals, and functions."""
    even_total = 0
    for value in values:
        if value % 2 == 0:
            even_total += 1
    return even_total


def safe_divide(dividend: float, divisor: float) -> float | None:
    """Handle potential runtime errors using exceptions."""
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    # Quick manual test when running ``python practice/basics.py``.
    collections = describe_collections()
    print(collections)
    print(format_candidate_summary("alex", ["problem solving", "teamwork"]))
    print(count_even_numbers([1, 2, 3, 4]))
    print(safe_divide(10, 0))
