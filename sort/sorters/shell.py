"""
shell.py
Shell sort implementation.
"""

from .sorter import Sorter


class ShellSorter(Sorter):
    """
    (factor of 4) Shell Sort
    -=-=-=-=-=-=-=
    A much much much much much much faster algorithm that
    not only takes the advantage of insertion sort, but
    actually augments its advantage. It pre-sorts the data
    into bigger chunks, then fine-tuning it.
    Implemented in Java @pg 259 as Algorithm 2.2.

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

        h = 1
        while h < len(self.data)/4:
            h = int(4*h)

        while h >= 1:
            for pointerIndx in range(1, len(self.data), h):
                for checkIndx in reversed(range(0, pointerIndx, h)):
                    try:
                        if self.data[checkIndx] > self.data[checkIndx+h]:
                            self._swap(checkIndx, checkIndx+h)
                        elif self.data[checkIndx] <= self.data[checkIndx+h]:
                            break
                    except IndexError:
                        break
            h = int(h/4)

        # Check the sorting
        assert self._check(), "This algorithm has done goof!"

        # Return sort
        return self.data

