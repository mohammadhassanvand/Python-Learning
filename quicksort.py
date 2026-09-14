"""
QuickSort (Lomuto partition scheme)
------------------------------------
Time complexity : Best/Average O(n log n), Worst O(n^2)
Space complexity: O(log n)  (recursion stack)

The array is sorted in place. The last element of each sub-array
is chosen as the pivot; elements smaller than the pivot are moved
to its left, larger ones to its right, then each side is sorted
recursively.
"""

from __future__ import annotations


def quicksort(arr: list[int], lo: int = 0, hi: int | None = None) -> list[int]:
    """Sort `arr` in place using QuickSort and return it."""
    if hi is None:
        hi = len(arr) - 1

    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

    return arr


def partition(arr: list[int], lo: int, hi: int) -> int:
    """Partition arr[lo..hi] around arr[hi] and return the pivot's final index."""
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    sample = [5, 2, 8, 1, 6, 3, 7, 4]
    print("before:", sample)
    quicksort(sample)
    print("after: ", sample)
