import pandas as pd
import skrf as rf
import numpy as np
import math

def get_decap_library(library_path = "data/decap_library_adapted.csv"):
    decap_frame = pd.read_csv(library_path, sep=";", names=["C", "ESL", "ESR"], skiprows=1)
    return decap_frame

def get_decap_network(decap, ntw_board):
    '''
    Only submit one decap as pandas series, not a data frame
    e.g. data_frame.loc[index] -> results in pandas series
    '''
    imp_array = np.zeros((len(ntw_board.f), 2, 2), dtype=np.complex128)
    capacitance = decap['C']
    esr = decap["ESR"]
    esl = decap["ESL"]
    for index, freq in enumerate(ntw_board.f):
        imp_array[index, 0, 0] = imp_array[index, 1, 1] = imp_array[index, 0, 1] = imp_array[index, 1, 0] = (esr) + (1j * freq*2*math.pi * esl) - (1j / (freq*2*math.pi * capacitance))
        # print(imp_array)

    freq = rf.Frequency.from_f(ntw_board.f, unit="Hz")
    ntw_decap = rf.Network(frequency = freq, z = imp_array, f_unit='Hz')
    return ntw_decap

def get_vrm_network(ntw_board, r = 0.05, l = 2e-9):
    imp_array = np.zeros((len(ntw_board.f), 2, 2), dtype=np.complex128)
    for index, freq in enumerate(ntw_board.f):
        imp_array[index, 0, 0] = imp_array[index, 1, 1] = imp_array[index, 0, 1] = imp_array[index, 1, 0] = (r) + (1j * freq*2*math.pi * l)

    freq = rf.Frequency.from_f(ntw_board.f, unit="Hz")
    return rf.Network(frequency = freq, z = imp_array, f_unit='Hz')

def connect_to_network(ntw_decap, ntw_board, board_port = 2):
    ntw_connected = rf.network.connect(ntw_board, board_port, ntw_decap, 0)
    return ntw_connected

def get_violation_frequency(ntw, port_interest = 1, target_impedance = 0.03):
    '''
        returns the first violation frequency based on the last frequency index lower than the target impedance,
        returns 0 if no violation
        return -1 if always violated
    '''
    idx = np.argwhere(np.diff(np.sign(abs(ntw.z[:, port_interest, port_interest]) - target_impedance))).flatten()
    if len(idx) == 0 and abs(ntw.z[0, port_interest, port_interest]) < target_impedance:
        return 0
    elif len(idx) == 0 and abs(ntw.z[0, port_interest, port_interest]) >= target_impedance:
        return -1
    else:
        return ntw.f[idx[0]]

def get_ntw_board(file = "data/ntw_board.s26p"):
    return rf.Network(file)