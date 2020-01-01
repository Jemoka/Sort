"""
__sorter_example.py
This is a dummy implementation of a sorter as simple reference.
"""

from .sorter import Sorter


class dummy(Sorter):
    """
    A sorter
    -=-=-=-=
    Some description of that sorter

    Publicly Callable Methods
    ================
    load(data:list)->list  Loads an array into the sorter's memory
    sort()->list  Sorts and returns loaded data, empties the sorter's memory

    Class Callable (Unexposed) Methods
    ================
    _swap(indxA, indxB) -> None  Swaps two indexes of the array loaded
    _check() -> bool  Checks if array in memory is sorted
    """

    def sort(self) -> list:
        """Sorts loaded data from least to most, and return sorted array"""
        super().sort()

        # Sort the data here, somehow
        # BOO BOO BOO BOO SORT SORT SORT
        # --------------------------

        # Check the sorting
        assert self._check(), "This algorithm has done goof!"

        # Return sort
        return self.data

