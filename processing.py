#!/usr/bin/env python3

import scipy.io
import numpy as np
from matplotlib import pyplot as plt

# full_dataset = scipy.io.loadmat("./nbi/test.mat")


def list_subsections(full_dataset):
    print("subsections (I'm using zerod by default):")
    print(full_dataset['post'].dtype)


def list_indexes(full_dataset, subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(full_dataset['post']['zerod'][0][0].dtype)


def get_variable(index, full_dataset, subsection='zerod'):
    a = full_dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(start, end, index, full_dataset, subsection='zerod'):
    a = get_variable(index, full_dataset, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))


# list_subsections()
# list_indexes()
# print(get_average(50, 100, 'te0'))
# plt.plot(get_variable('te0'))
# plt.show()
