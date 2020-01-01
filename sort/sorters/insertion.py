"""
insertion.py
Insertion Sort Implementation
"""

from .sorter import Sorter


class InsertionSorter(Sorter):
    """
    Insertion Sort
    -=-=-=-=-=-=-=
    A much much much faster algorithm that takes advantage
    of the relations of the input array. It also gets faster 
    as more of the array is sorted — much faster than a
    linear relationship.
    Algorithm 2.2 in the book. Java implementation @pg 251.

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

        for pointerIndx in range(1, len(self.data)):
            for checkIndx in reversed(range(0, pointerIndx)):
                if self.data[checkIndx] > self.data[checkIndx+1]:
                    self._swap(checkIndx, checkIndx+1)
                elif self.data[checkIndx] <= self.data[checkIndx+1]:
                    break
        # Starting from the second item, range(1, len(self.data)),
        # keep swapping backwards until it is in order.
        # Notice! This is implemented with checkIndx, which is in
        # descending order starting from the current digit
        # which is for looped backwards until (maximumly), zero.
        # If the digit is not in place, swap it with the one before.
        # If it is, then stop iterating checkIndx and move the pointer
        # onto the next item.

        # Check the sorting
        assert self._check(), "This algorithm has done goof!"

        # Return sort
        return self.data

