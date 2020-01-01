"""
sorter.py
This is the base sorter — the abstract class from which
all other sorters will be drawn. You should really be looking at this
if you are trying to see the methods that each sorter in this package
must have. The actual sorters are located in parallel with this
file by its name.
"""

from abc import ABC, abstractmethod


class Sorter(ABC):
    def __init__(self):
        super().__init__()
        self.data = None

    def _swap(self, indxA, indxB) -> None:
        """Swaps the loaded data at two indexes"""
        assert self.data, "No data loaded!"
        oldA = self.data[indxA]
        oldB = self.data[indxB]
        self.data[indxB] = oldA
        self.data[indxA] = oldB

    def _check(self) -> bool:
        """Check if sorting is correct from least to most"""
        assert self.data, "No data loaded!"

        # Check of list is in ascending order
        for i in range(len(self.data)-1):
            if (self.data[i] < self.data[i+1]) is not (self.data[i] == self.data[i+1]):
                pass
            else:
                return False
        return True

    def load(self, data: list) -> list:
        """Loads data into the memory"""
        self.data = data

    @abstractmethod
    def sort(self) -> list:
        """Sorts loaded data from least to most, and return sorted array"""
        assert self.data, "No data loaded!"

