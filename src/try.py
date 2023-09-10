from datetime import datetime
from typing import List

def dates():
    print(" ")
    print(datetime(2022, 11, 24, 10, 33, 30, 0))
    print(" ")

    s = {4}
    x = 4
    if x in s:
        s.remove(x)
    print(s)


def change(lst: List[int]):
    lst.append(0)
    lst = []


if __name__ == "__main__":
    lst1 = [1, 2, 3]
    change(lst1)
    print(lst1)
