#!/usr/bin/python3
def multiple_returns(sentence):
    res = ()
    if len(sentence) == 0:
        res = (0, None)
        return res
    else:
        res = (len(sentence), sentence[:1])
        return res
