from typing import Set, Optional, List


# Napište čistou funkci, která najde libovolnou podmnožinu zadané množiny
# kladných celých čísel ‹nums›, součet jejíchž prvků je přesně
# ‹total›. Pokud taková podmnožina neexistuje, funkce vrátí ‹None›.


def combinations(a: List[int]) -> List[List[int]]:
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combinations(a[1:]):
        cs += [c, c+[a[0]]]
    return cs


def subset_sum(nums: Set[int], total: int) -> Optional[Set[int]]:
    if len(nums) == 0 and total:
        return None
    if len(nums) == 1 and total in nums:
        return nums
    elements = combinations(list(nums))
    for elem in elements:
        if sum(elem) == total:
            return set(elem)
    return None


def main() -> None:
    assert subset_sum(set(), 5) is None
    assert subset_sum({1, 2, 3}, 7) is None
    assert subset_sum({1}, 1) == {1}
    assert subset_sum({1, 2, 3}, 5) == {2, 3}
    assert subset_sum({5, 10, 12, 13}, 27) == {5, 10, 12}


if __name__ == '__main__':
    main()
