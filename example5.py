from typing import Any


def talk(input_parameter: Any) -> None:
    print("The input is: " + str(input_parameter))


talk("hi")
talk(5)
talk([2, 5, 6])
