#!/usr/bin/python3
def remove_char_at(str, n):
    buf = ""
    for i in range(len(str)):
        if i != n:
            buf += str[i]
    return buf
