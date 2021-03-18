from random import shuffle

def sort(list_, key=None):
    """
    Sorts a given list.

    `list_`: an iterable to be sorted
    `key`: a callable that returns the sorting key for a given item, optional    

    This is an implementation of the famous bogosort, the most inefficient
    sort ever, it shuflles the input list until it is sorted.
    """

    while sorted(list_, key=key) != list_:
        shuffle(list_)

    return list_