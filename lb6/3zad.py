from collections import Counter

import pylab
from matplotlib import pyplot as plt
import numpy as np


def create_sentence_histogram(sentence: str):
    symbols = ['...', '.', '!', '?']
    for i in range(0, len(symbols)):
        pylab.bar(symbols[i], sentence.count(symbols[i]))
    pylab.show()

create_sentence_histogram("Я человек?Я пойду туда!Он не будет это есть.Он умер ...")