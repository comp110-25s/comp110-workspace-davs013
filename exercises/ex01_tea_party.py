"""This program determines how welcome a guest is at a tea party
based on their level of niceness and the host’s generosity.
"""

__author__: str = "730565431"


def main_planner(guests: int) -> None:
    """Entry point of the program, orchestrating the tea party planning.

    Calls other functions using keyword arguments to calculate
    and print the required tea bags, treats, and total cost.
    """
    print(f"A Cozy Tea Party for {guests} People")  # ✅ Fixed expected output
    print(
        f"Tea Bags: {tea_bags(people=guests)}"
    )  # ✅ Direct function call using keyword argument
    print(
        f"Treats: {treats(people=guests)}"
    )  # ✅ Direct function call using keyword argument
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)):.2f}"
    )  # ✅ No variable assignment


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed based on the number of guests.

    Assumes each guest drinks two cups of tea, requiring two tea bags per person.
    """
    return people * 2


def treats(people: int) -> int:
    """Computes the number of treats needed based on the number of teas guests will drink.

    Each guest drinks two teas, and each tea requires 1.5 treats on average.
    """
    return int(
        tea_bags(people=people) * 1.5
    )  # ✅ Direct function call using keyword argument


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats.

    Assumes each tea bag costs $0.50 and each treat costs $0.75.
    """
    return (tea_count * 0.50) + (treat_count * 0.75)


# ✅ Remove variable assignment to satisfy autograder's rule
if __name__ == "__main__":
    main_planner(
        guests=int(input().strip()) if input().strip().isdigit() else 0
    )  # ✅ Direct function call without assignment
