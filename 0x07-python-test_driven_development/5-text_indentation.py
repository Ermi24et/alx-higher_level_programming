#!/usr/bin/python3

"""
module that prints a text with 2 new lines after
the characters ., ? and :
module for 5-text_indentations
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline = True

    for i in text:
        if newline and i == ' ':
            continue
        newline = False

        print(i, end='')
        if i in ".?:":
            print("\n")
            newline = True
