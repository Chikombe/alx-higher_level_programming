#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    import sys

    total = 0
    for itr in range(len(sys.argv) - 1):
        total += int(sys.argv[itr + 1])
    print("{}".format(total))
