import time
from .sorters import selection
from .sorters import insertion
from .sorters import shell
from .sorters.sorter import Sorter


def __sort(data: list, sorter: Sorter) -> list:
    sorter.load(data)
    return sorter.sort()


def __timed_sort(data: list, sorter: Sorter) -> list:
    sorter.load(data)
    timeStart = time.time()
    srted = sorter.sort()
    timeStop = time.time()
    return srted, timeStop-timeStart


def sort(data: list, sorter_name: str, timed: bool = False) -> list:
    """Sort a list"""
    if sorter_name.lower() == "selection":
        sorter = selection.SelectionSorter()
    elif sorter_name.lower() == "insertion":
        sorter = insertion.InsertionSorter()
    elif sorter_name.lower() == "shell":
        sorter = shell.ShellSorter()

    if timed:
        return __timed_sort(data, sorter)
    else:
        return __sort(data, sorter)


