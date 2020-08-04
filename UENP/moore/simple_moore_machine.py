"""Simple Moore Machine

This is a simple Moore Machine where it read only 'a' and 'b' charfield
and returns a cached output and the state what stopped.
"""

import collections
import typing


class SimpleMooreMachine:
    """Simple Moore Machine

    This class handle the machine stuff.
    """

    def __init__(self, string: str):
        self.input = self._validate_data(string)
        self._state = 0  # @property
        self._counter = collections.Counter()
        self._cache = []
        self._outpout_data = []

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

            # Reaches a state and call output logic
            self._make_output(char)

            self._cache.append((
                f"State: {self._state}",
                f"Times it was called: {self._counter[char]}"
            ))

    def _make_output(self, letter: str):
        """Make Output

        Note:
            Just make the output logic.

        Args:
            letter: Receive 'a' or 'b'.
        """

        a = 'YOU CHOSE AAAAA'
        b = 'YOU CHOSE BBBBB'

        if letter == 'a':
            self._outpout_data.append(a)
        else:
            self._outpout_data.append(b)

    def show_output_data(self):
        """Show Output Data

        Note:
            Preferably, use it after execute machine.

        Returns:
            Returns self._outpout_data.
        """
        return f"Output Data: {self._outpout_data}"

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
    moore = SimpleMooreMachine(string)
    moore.execute_machine()  # Run Machine

    print_in_line(moore.pretty_print_states())  # Print States
    print_in_line(moore.show_cached_data())  # Print Cache

    print(f"Final State: {moore.final_state()}")  # Print Final State

    print(moore.show_output_data())


if __name__ == '__main__':
    _run_code('ababa')
