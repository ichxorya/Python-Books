# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:26:57 2022

@author: Ichxorya
"""


def pig_latin(_input: str):
    punc = ""
    if _input[-1] in ".!?":
        punc = _input[-1]
        _input = _input[0 : len(_input) - 1]

    if _input[0] in "aeiouAEIOU":
        return _input + "way" + punc
    # Python -> Ythonpay
    if _input[0].isupper():
        _input = (
            _input[0].swapcase()
            + _input[1].swapcase()
            + _input[2 : len(_input)]
        )
    return _input[1 : len(_input)] + _input[0] + "ay" + punc


def pl_sentence(sentence):
    sentence_as_list = sentence.split()
    output = list()
    for i in sentence_as_list:
        output.append(pig_latin(i))

    return " ".join(output)


print(pl_sentence("this is a test translation"))
