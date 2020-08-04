"""Simple Mealy Machine

This is a simple Mealy Machine where it read only 'a' and 'b' charfield
and returns a cached output and the state what stopped.
"""

import collections
import typing


class SimpleMealyMachine:
    """Simple Mealy Machine

    This class handle the machine stuff.
    """

    def __init__(self, string: str):
        self.input = self._validate_data(string)
        self._state = 0  # @property
        self._counter = collections.Counter()
        self._cache = []

    @staticmethod
    def _validate_data(value: str):
        """Validate Data

        Note:
            Here checks if the user is using the letters 'a' or 'b'
            if have other wrong letters raise a error.

        Args:
            value: Is a string input.

        Returns:
            Returns the value in lower case.
        """

        if not set(value) == {'a', 'b'}:
            raise ValueError("We just accept letters 'a' and 'b'.")

        return value.lower()

    def execute_machine(self):
        """Execute Machine

        Just execute the logic machine.
        """

        for char in self.input:
            self._counter[char] += 1

            self._state = 1
            if char == 'b':
                self._state = 2

            self._cache.append((
                f"State: {self._state}",
                f"Times it was called: {self._counter[char]}"
            ))

    def final_state(self):
        """Final State

        Note:
            Use it after execute machine.

        Returns:
            Returns the final state.
        """
        return self._state

    def pretty_print_states(self):
        """Pretty Print States

        Returns:
            Returns self._counter with a pretty format.
        """
        return {
            'State 1 (a)': f"{self._counter['a']} times",
            'State 2 (b)': f"{self._counter['b']} times",
        }

    def show_cached_data(self):
        """Show Cached Data

        Note:
            Preferably, use it after execute machine.

        Returns:
            Returns self._cache.
        """
        return self._cache


def print_in_line(data: typing.Union[list, dict]):
    """Print In Line

    Just print the data in line.
    """
    for pretty_print in data:
        print(pretty_print)


def _run_code(string: str):
    """Run Code

    Just a example running the code.
    """
    mealy = SimpleMealyMachine(string)
    mealy.execute_machine()  # Run Machine

    print_in_line(mealy.pretty_print_states())  # Print States
    print_in_line(mealy.show_cached_data())  # Print Cache

    print(f"Final State: {mealy.final_state()}")  # Print Final State


if __name__ == '__main__':
    _run_code('ababa')
