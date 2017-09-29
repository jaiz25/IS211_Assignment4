#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment 4; comparing search"""


import time


def sequential_search(a_list, item):

    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time()
    return found, end-start


def ordered_sequential_search(a_list, item):

    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            stop = True
        else:
            pos = pos+1
    end = time.time()
    return found, end-start


def binary_search_iterative(a_list, item):

    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    end = time.time()
    return found, end-start


def binary_search_recursive(a_list, item):

    a_list.sort()

    start = time.time()

    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

    end = time.time()
    return end-start


def main():

    for i in range(100):
        print "Sequential Search found %d items; took %10.7f seconds to run (size - 500)." \
            % sequential_search(range(500), -1)
        print "Ordered Sequential Search found %d items; took %10.7f seconds to run (size - 500)." \
            % ordered_sequential_search(range(500), -1)
        print "Binary Search Iterative found %d items; took %10.7f seconds to run (size - 500)." \
            % binary_search_iterative(range(500), -1)
        print "Binary Search Recursive found items; took %10.7f seconds to run (size - 500)." \
            % binary_search_recursive(range(500), -1)

        print '-' * 100

        print "Sequential Search found %d items; took %10.7f seconds to run (size - 1,000)." \
            % sequential_search(range(1000), -1)
        print "Ordered Sequential Search found %d items; took %10.7f seconds to run (size - 1,000)." \
              % ordered_sequential_search(range(1000), -1)
        print "Binary Search Iterative %d took %10.7f seconds to run (size - 1,000)." \
              % binary_search_iterative(range(1000), -1)
        print "Binary Search Recursive found items; took %10.7f seconds to run (size - 1,000)." \
              % binary_search_recursive(range(1000), -1)

        print '-' * 100

        print "Sequential Search found %d items; took %10.7f seconds to run (size - 10,000)." \
            % sequential_search(range(10000), -1)
        print "Ordered Sequential Search found %d items; took %10.7f seconds to run (size - 10,000)." \
              % ordered_sequential_search(range(10000), -1)
        print "Binary Search Iterative found %d items; took %10.7f seconds to run (size - 10,000)." \
              % binary_search_iterative(range(10000), -1)
        print "Binary Search Recursive found items; took %10.7f seconds to run (size - 10,000)." \
              % binary_search_recursive(range(10000), -1)


if __name__ == "__main__":
    main()

