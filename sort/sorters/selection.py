"""
selection.py
Selection Sort Implementation
"""

import operator
from .sorter import Sorter


class SelectionSorter(Sorter):
    """
    Selection Sort
    -=-=-=-=-=-=-=
    Perhaps the simplest algorithm. Demonstrated as Algorithm 2.1
    in the book. The Java implementation is located @pg 249.

    Publicly Callable Methods
    ================
    load(data:list)->list  Loads an array into the sorter's memory
    sort()->list  Sorts and returns loaded data, empties the sorter's memory

    Class Callable (Unexposed) Methods
    ================
    _swap(indxA, index) -> None  Swaps two indexes of the array loaded
    _check() -> book  Checks if array in memory is sorted
    """

    def sort(self) -> list:
        """Sorts loaded data from least to most, and return sorted array"""
        super().sort()

        # Data Sorting
        for indx, i in enumerate(self.data):
            # Find the index of the maximum value in the set from the position
            # of i to the end of the array

            minIndexSub = self.data[indx:].index(min(self.data[indx:]))
            minIndex = minIndexSub+indx

            # OK.... This mess will take a bit of explanation.
            # Let's take the first variable apart in the same order
            # that an interpreter will read it.
            # ----------------------------------------------
            # Selection sort "selects" (get it?)
            # the max/min of a incrementally smaller list, thus creating a
            # sorted list. Please see pp249's trace in the Algorithms book.
            # ----------------------------------------------
            # -> self.data[indx:]) gets a sublist of data, starting @ the index
            # that is being considered. min, obviously, finds min. Now,
            # remember that this is the minimum of the sublist as min() is
            # wrapped around self.data[-->indx:], and not the
            # full list self.data. Hence, the .index() will be taken
            # with the sublist. With this, minListSub is the index of the
            # minimum within the sublist. Then, minList is that sublist
            # index + the items "unconsidered" within the full list self.data,
            # which of course, happens to be indx. So minList is minListSub+
            # indx, which is the index of the minimum in the larger list.

            self._swap(indx, minIndex)
        # --------------------------

        # Check the sorting
        assert self._check(), "This algorithm has done goof!"

        # Return sort
        return self.data

