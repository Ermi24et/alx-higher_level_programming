#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    mem = dir(hidden_4)
    num = len(mem)
    for i in range(0, num):
        if mem[i].startswith('_'):
            continue
        else:
            print("{}".format(mem[i]))
