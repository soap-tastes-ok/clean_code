import time


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

# main, qsort, bsortは同じなので省略
# ①の機能の実装
class Sorter:
    def __init__(self):
        pass

    def sort(self, a):
        raise NotImplementedError()


class QuickSorter(Sorter):
    def __init__(self):
        pass

    def sort(self, a):
        return qsort(a)


class BubbleSorter(Sorter):
    def __init__(self):
        pass

    def sort(self, a):
        return bsort(a)


# ②の機能拡張
# QuickSorterはSorterを継承しているため、TimerSorterでsortするには再度継承が必要
# (クラス名も変更の必要がある)
class TimerSorter(Sorter):
    def __init__(self):
        pass

    def timesort(self, a):
        start = time.time()
        a_sorted = self.sort(a)
        print(time.time() - start)
        return a_sorted


class TimeQuickSorter(TimerSorter):
    def __init__(self):
        pass

    def sort(self, a):
        return qsort(a)


class TimeBubbleSorter(TimerSorter):
    def __init__(self):
        pass

    def sort(self, a):
        return bsort(a)
