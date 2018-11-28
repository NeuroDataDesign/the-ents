# Ganesh Arvapalli
# 11/26/18

import numpy as np
import h5py

def make_matrix(filename):
    h5f = h5py.File(filename, 'r')
    data = h5f['data'][:]
    patient_list = h5f['patient-list'][:]
    h5f.close()
    return data, patient_list

def main():
    print(make_matrix('./HNU1.h5'))

if __name__ == "__main__": main()
