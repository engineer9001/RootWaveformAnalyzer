import uproot
import numpy as np

from os import listdir


def openWaveforms(keyword, directory, rmBackground=False, FFT=False):
    """
    A function for parsing through a directory of root files, opening every file in the directory, parsing through every object in each root file, and then returning an array of the 2nd axis of information conent of each object in the root file that contains a certain string (keyword) in the object name. Designed to access the time-series vector of waveforms saved as a TGraph with constant spacing in time.

    Args:
        keyword (string): the identifying string in the name of each root object whose content is desired
        directory (string): location of the directory containing all root files to be looped over
        rmBackground (bool): if True, subtracts the median of the first 20 elements in the time series from all points
        FFT (bool): if True, returns the discrete Fourier Transform of the waveform

    Returns:
        waveforms (list): A list of numpy arrrays each of which corresponds to a single waveform that has been extraceted from the root files in the given directory. 
    """
    #sift through root files and put all time series arrays in a single array

    files = listdir(directory)
    #print(files)

    waveforms = []
    for i in files:
        file  = uproot.open("rootWaveforms/" + i)
        for j in file.keys():
            if keyword in j:
                waveforms.append(file[j[:-2]].values()[1])

    waveforms = np.array(waveforms) #all my imported waveforms

    if rmBackground:
        for i in range(len(waveforms)):
            med = np.median(waveforms[i][:20])
            waveforms[i] = waveforms[i] - med
    
    if FFT:
        for i in range(len(waveforms)):
            waveforms[i] = np.real(np.fft.fft(waveforms[i]))

    return waveforms


