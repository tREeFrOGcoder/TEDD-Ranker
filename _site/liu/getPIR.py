import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def transform(same_bench_pir=0, oth_bench_pir=0):
    # linear reg. for same_brench
    if same_bench_pir != 0 :
        model_same_bench = LinearRegression()
        X = np.array([0.949,1.01])
        Y = np.array([1.284,1.475])
        model_same_bench.fit(X.reshape(-1,1), Y.reshape(-1,1))
        win_same_pir = float(model_same_bench.predict(np.array(same_bench_pir).reshape(-1,1)))
        return win_same_pir
    
    # linear reg. for other_brench
    elif oth_bench_pir != 0 :
        model_oth_bench = LinearRegression()
        X = np.array([0.985,1.000])
        Y = np.array([1.344,1.426])
        model_oth_bench.fit(X.reshape(-1,1), Y.reshape(-1,1))
        win_same_pir = float(model_oth_bench.predict(np.array(oth_bench_pir).reshape(-1,1)))
        return win_same_pir


"""
type: a string choose from ["same_win", "same_bench", "other_bench"]. Corresponding to the four settings provided (There is no operation for the category: "other_win", becasue it is neither common nor useful)
SEM: a list that contain the win-tie-loss or benchmark score of each SEM under different settings
BM: a list that contain the win-tie-loss or benchmark score of each BM under different settings
pir: a list that contain the PIR under different settings

one can provide pure pir or (SEM, BM) pair to get the PIR.
"""
def getPIR(type:str, SEM:list = None, BM:list = None, pir:list = None):
    if pir is None:
        pir = np.average(np.array(SEM)/np.array(BM))
        if type == "same_win":
            PIR = pir
        if type == "same_bench":
            PIR = transform(same_bench_pir=pir)
        if type == "other_bench":
            PIR = transform(oth_bench_pir=pir)
    else:
        if type == "same_win":
            PIR = pir
        if type == "same_bench":
            PIR = transform(same_bench_pir=pir)
        if type == "other_bench":
            PIR = transform(oth_bench_pir=pir)
    print(PIR)
    return PIR
    
# some examples:
getPIR(SEM=[1.2, 3], BM=[1.2], type = "same_win")
# getPIR(SEM=[1.2, 3], BM=[3], type = "same_win")
# getPIR(SEM=[1.2, 3], BM=[1,4], type = "same_bench")