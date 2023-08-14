#!/usr/bin/python3

def add_tuple(tuple_a = (), tuple_b = ()):
    add_tuple = []
    if len(tuple_a) > 2:
        for i in range(len(tuple_a)):
            add_tuple.append(tuple_a[i] + tuple_b[i])
    else:
        if len(tuple_a) < 1:
            tuple_a = (0, 0)
        elif len(tuple_a) < 2:
            tuple_a = (tuple_a[0], 0)
        if len(tuple_b) < 1:
            tuple_b = (0, 0)
        elif len(tuple_b) < 2:
            tuple_b = (tuple_b[0], 0)
        add_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    add_tuple = tuple(add_tuple)
    return add_tuple
