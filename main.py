import math as m
import numpy as np


def print_hi(name):
    print(f'Hi, {name}')
    print("john john".replace("john", "John", 1))
    print(__name__)
    arr = np.array([1, 2, 3])
    arr2 = np.array([1, 3, 0])
    print(np.concatenate([arr, arr2]))
    print(np.vstack([arr, arr2]))
    print(np.hstack([arr, arr2]))


# print(np.vstack(arr2))
# print(np.hstack(arr2))
# print(arr.argsort()[-len(arr):][::-1])


if __name__ == '__main__':
    print_hi('PyCharm')
