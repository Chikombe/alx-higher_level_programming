#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys

    arg = sys.argv
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(count))
    for itr in range(count):
        print("{}: {}".format(itr + 1, sys.argv[itr + 1]))
