# RootWaveformAnalyzer
A package designed to allow one to open a number of waveform objects saved in a root file as TGraph objects and do some shape analyses among them including a UMAP projection to a 2-dimensional space. Additionally included is a script for making a dynamic time warp matrix comparing every pair of waveforms in a sample.

# Required Packages

matplotlib (3.6.2)

uproot (4.3.7)
 
numpy (1.23.4)

umap (0.5.3)

(Other versions will very likely be compatible)

# Installation Instructions

Download all scripts and required pythong packages. 

Most important is grabRootWaveForms.py which is responsible for opening the root file(s) so they can be easily interpreted by python. In this file is a function (openWaveforms) that takes a keyword and a directory location which will scan through the given directory location, open every root file in that directory, and then extract the values of every waveform in each root file whose title contains the given keyword. The function then returns a list of vectors where each vector is the values of each time-series waveform.


