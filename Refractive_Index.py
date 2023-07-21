# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:53:51 2023

@author: Ari
"""

# imports
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# retrieving data from csv file
# INPUT DATA FILE NAME IN LINE BELOW
df = pd.read_csv("testdata.csv").values


# variables
substrate_transmittance = np.zeros(len(df))
sample_transmittance = np.zeros(len(df))
wavelength = np.zeros(len(df))
sample_name = input("What is the sample name? ")

# extracting data from data frame
for i in range(len(df)):
    substrate_transmittance[i] = df[i, 0]
    sample_transmittance = df[i, 1]
    wavelength[i] = df[i, 2]

# defining value of Ts
Ts = np.average(substrate_transmittance)

# calculating substrate refractive index
s = (1/Ts) + np.sqrt((1/(Ts**2)) - 1)

# finding sample transmittance peaks
transmittance_peak_indices = sp.signal.find_peaks(sample_transmittance)
transmittance_peak_values = np.zeros(100)
wavelength_peak_values = np.zeros(100)
for i in range(len(transmittance_peak_indices)):
    transmittance_peak_values[i] = sample_transmittance[transmittance_peak_indices[i]]
    wavelength_peak_values[i] = wavelength[transmittance_peak_indices[i]]
    
# filtering out zero values from peak values
index = 0 
idx = []
for transmittance_peak_values[i] in transmittance_peak_values:
    if transmittance_peak_values[i] == 0:
        idx.append(index)
    index += 1

# deleting 0 values    
transmittance_peak_values = np.delete(transmittance_peak_values, idx)
wavelength_peak_values = np.delete(wavelength_peak_values, idx)


# finding sample transmittance troughs
transmittance_trough_indices = sp.signal.find_peaks(-sample_transmittance)
transmittance_trough_values = np.zeros(100)
wavelength_trough_values = np.zeros(100)

for i in range(len(transmittance_trough_indices)):
    transmittance_trough_values[i] = sample_transmittance[transmittance_trough_indices[i]]
    wavelength_trough_values[i] = wavelength[transmittance_trough_indices[i]]
    
# filtering out zero values from trough values
index = 0 
idx = []
for transmittance_trough_values[i] in transmittance_trough_values:
    if transmittance_trough_values[i] == 0:
        idx.append(index)
    index += 1

# deleting 0 values    
transmittance_trough_values = np.delete(transmittance_trough_values, idx)
wavelength_trough_values = np.delete(wavelength_trough_values, idx)


# defining curve fits for TM and Tm
def peak_curve_fit(x, A, B, C, D):
    return (A*x) / (B - C*x + D*(x**2))

def trough_curve_fit(x, A, B, C, D):
    return (A*x) / (B + C*x + D*(x**2))


# finding curve fit parameters
peakpopt, peakpcov = sp.optimize.curve_fit(peak_curve_fit, wavelength_peak_values, transmittance_peak_values)
troughpopt, troughpcov = sp.optimize.curve_fit(trough_curve_fit, wavelength_trough_values, transmittance_trough_values)


def refractive_index(x):
    '''This function takes a wavelength value, x, and returns the refractive 
    index at that point.'''
    TM = (peakpopt[0]*x) / (peakpopt[1] - peakpopt[2]*x + peakpopt[3]*(x**2))
    Tm = (troughpopt[0]*x) / (troughpopt[1] - troughpopt[2]*x + troughpopt[3]*(x**2))
    N = ((2*s*(TM - Tm)) / (TM*Tm)) + (s**2 + 1) / 2
    n = np.sqrt(N + np.sqrt(N**2 - s**2))
    
    return n

# assigning refractive index data values for plotting
refractive_index_data = refractive_index(wavelength)

# plotting wavelength vs refractive index
fig, ax = plt.subplots(figsize = (10,8)) 
plt.scatter(wavelength, refractive_index_data)
plt.title("Refractive index of {}" .format(sample_name))
plt.xlabel("Wavelength, nm")
plt.ylabel("Refractive index, n")
plt.show() 