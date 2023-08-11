#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n - 1 == 1:
        print("1 argument:")
    elif n - 1 == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(n - 1, "arguments"))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
