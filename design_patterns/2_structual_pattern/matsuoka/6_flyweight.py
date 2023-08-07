import sys


def main():
    r, g, b = "red", "green", "blue"

    # Tupleにstringの文字列を代入
    tuple1 = ("red", "green", "blue", "red", "green", "blue", "red", "green")
    # 5行目で定義した変数をタプルで参照している
    # メモリの使用量を削減可能
    tuple2 = (r, g, b, r, g, b, r, g)

    # calc memory size(tuple1)
    memorysize_tuple1 = 0
    memorysize_tuple1 += sys.getsizeof(tuple1)
    for item in tuple1:
        memorysize_tuple1 += sys.getsizeof(item)

    # calc memory size(tuple2)
    memorysize_tuple2 = 0
    memorysize_tuple2 += sys.getsizeof(tuple2)
    for item in [r, g, b]:
        memorysize_tuple2 += sys.getsizeof(item)

    print(memorysize_tuple1, memorysize_tuple2)


if __name__ == "__main__":
    main()
