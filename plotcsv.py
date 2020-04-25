#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog

if __name__ == "__main__":
    if len(sys.argv) < 2:
        root = tk.Tk()
        root.withdraw()
        fnames = filedialog.askopenfilenames(
            parent=root,
            title='Select one or more files',
            filetypes=(("CSV Files", "*.csv"), ("All files", "*.*"))
        )
        root.destroy()
    else:
        fnames = sys.argv[1:]
    for fname in fnames:
        with open(fname) as f:
            line = f.readline()
            labels = line.split(',')
        data = np.loadtxt(fname, delimiter=',', skiprows=1)
        for i in range(data.shape[1]):
            plt.plot(data[:,i], label=labels[i])
    if len(fnames) > 0:
        plt.grid()
        plt.legend()
        plt.show()
