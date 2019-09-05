# A jitter function   
# Implemented based on https://github.com/wch/r-source/blob/5a156a0865362bb8381dcd69ac335f5174a4f60c/src/library/base/R/jitter.R 
# Tejus <tejzpr@gmail.com>
import numpy as nm
import math

def jitter(x, factor = 1, amount = None):
    if len(x) == 0:
        return x
    try:
        numTest = all(isinstance(round(i), int) for i in x)
        if numTest == False:
            raise Exception("'x' must be a list of numeric values")
    except:
        raise Exception("'x' must be a list of numeric values")

    z = max(x) - min(x)
    if z == 0:
        z = min(x) if min(x) > 0 else 1

    if amount == None:
        xUniqs = sorted(list(set([round(elem, 3 - math.floor(math.log10(z))) for elem in x])))
        d = nm.diff(xUniqs)
        if len(d) > 0:
            d = min(d)
        else:
            d = z/10
        amount = factor/5 * abs(d)
    elif amount == 0:
        amount = factor * (z/50)

    K = nm.random.uniform((-1*amount),amount,(len(x),))
    return [sum(i) for i in zip(x, K)] 
