import numpy as np
import operator

def get_data():
    df = open("data_set.txt")
    set_context = df.readlines()