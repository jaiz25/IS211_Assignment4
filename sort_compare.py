#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment 4; comparing sorts"""


from timeit import Timer


def insertion_sort(a_list):

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


def shell_sort(a_list):

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):

    a_list.sort()


def main():

    t1 = Timer("insertion_sort(range(500))", "from __main__ import insertion_sort")
    print "Insertion sort took", t1.timeit(number=100), "milliseconds (size - 500)."

    t1 = Timer("insertion_sort(range(1000))", "from __main__ import insertion_sort")
    print "Insertion sort took", t1.timeit(number=100), "milliseconds (size - 1,000)."

    t1 = Timer("insertion_sort(range(10000))", "from __main__ import insertion_sort")
    print "Insertion sort took", t1.timeit(number=100), "milliseconds (size - 10,000)."

    print '-' * 100

    t2 = Timer("shell_sort(range(500))", "from __main__ import shell_sort")
    print "Shell sort took", t2.timeit(number=100), "milliseconds (size - 500)."

    t2 = Timer("shell_sort(range(1000))", "from __main__ import shell_sort")
    print "Shell sort took", t2.timeit(number=100), "milliseconds (size - 1,000)."

    t2 = Timer("shell_sort(range(10000))", "from __main__ import shell_sort")
    print "Shell sort took", t2.timeit(number=100), "milliseconds (size - 10,000)."

    print '-' * 100

    t3 = Timer("python_sort(range(500))", "from __main__ import python_sort")
    print "Python sort took", t3.timeit(number=100), "milliseconds (size - 500)."

    t3 = Timer("python_sort(range(1000))", "from __main__ import python_sort")
    print "Python sort took", t3.timeit(number=100), "milliseconds (size - 1,000)."

    t3 = Timer("python_sort(range(10000))", "from __main__ import python_sort")
    print "Python sort took", t3.timeit(number=100), "milliseconds (size - 10,000)."


if __name__ == "__main__":
    main()

