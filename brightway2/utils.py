# -*- coding: utf-8 -*-
import random
import re
import string

# Maximum value for unsigned integer stored in 4 bytes
MAX_INT_32 = 4294967295


def natural_sort(l):
    """Sort the given list in the way that humans expect"""
    # http://nedbatchelder.com/blog/200712/human_sorting.html#comments
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def random_string(length):
    return ''.join(random.choice(string.letters + string.digits
        ) for i in xrange(length))
