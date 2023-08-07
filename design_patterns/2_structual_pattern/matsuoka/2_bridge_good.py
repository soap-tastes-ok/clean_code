import time


def main():
    exaple_list = [2, 7, 3, 4, 9, 1]
    sorter_quick = Sorter(QuickSorter())
    print(sorter_quick.sort(exaple_list))

    sorter_bubbl = Sorter(BubbleSorter())
    print(sorter_bubbl.sort(exaple_list))

    sorter_quick_timer = TimeSorter(QuickSorter())
    print(sorter_quick_timer.timesort(exaple_list))

    sorter_bubbl_timer = TimeSorter(BubbleSorter())
    print(sorter_bubbl_timer.timesort(exaple_list))


###############
# バブルソート
def bsort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]

    return a


# クイックソート
def qsort(a):
    if len(a) in (0, 1):
        return a

    p = a[-1]
    left = [x for x in a[:-1] if x <= p]
    right = [x for x in a[:-1] if x > p]

    return qsort(left) + [p] + qsort(right)


###############


class SortImple:
    def sort(self, a):
        raise NotImplementedError


class QuickSorter(SortImple):
    def __init__(self):
        pass

    def sort(self, a):
        return qsort(a)


class BubbleSorter(SortImple):
    def __init__(self):
        pass

    def sort(self, a):
        return bsort(a)


# ①の機能の実装
class Sorter:
    def __init__(self, sorter: SortImple):
        self.sorter = sorter

    def sort(self, a):
        return self.sorter.sort(a)


# ②の機能拡張
class TimeSorter(Sorter):
    def timesort(self, a):
        start = time.time()
        a_sorted = self.sorter.sort(a)
        print(time.time() - start)
        return a_sorted


if __name__ == "__main__":
    main()
