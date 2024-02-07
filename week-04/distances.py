# %% [mkarkdown]
# ---
# title: distances.py
# ---

# %%


def euclidean(pnt1, pnt2):
    dx = pnt1[0] - pnt2[0]
    dy = pnt1[1] - pnt2[1]
    return (dx**2 + dy**2) ** (1 / 2)


import numpy


def manhattan(pnt1, pnt2):
    dx = pnt1[0] - pnt2[0]
    dy = pnt1[1] - pnt2[1]
    adx = numpy.abs(dx)
    ady = numpy.abs(dy)
    return adx + ady


def distance_composite(pnt1, pnt2, metric="euclidean"):
    if metric == "euclidean":
        return euclidean(pnt1, pnt2)
    else:
        return manhattan(pnt1, pnt2)
