from grabRootWaveforms import openWaveforms
import numpy as np

import matplotlib.pyplot as plt

waveforms = openWaveforms("Cherenkov", "rootWaveforms")


for i in range(len(waveforms)):
    med = np.median(waveforms[i][:20])
    waveforms[i] = waveforms[i] - med



def dtw(s, t):
    """
    Implimentation of a Dynamic Time Warp distance calculation between two time-series vectors s & t

    Args:
        s (vector<number>): First time-series waveform
        t (vector<number>): Second time-series waveform

    Returns
        dtw_matrix[n][m] (number): The [n][m]th (bottom right-most) element of the dtw matrix which corresponds to the distance between waveforms when best-mateched to one-another as determined by the DTW

    
    """
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            # take last min from a square box
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix[n][m]



nloops = len(waveforms) * (len(waveforms)-1)/2
counter = 0
DTWMatrix = np.zeros((len(waveforms), len(waveforms)))
for i in range(len(waveforms)):
    for j in range(i):
        print("Completed " + str(counter) + " loops out of " + str(nloops))
        DTWMatrix[i][j] = dtw(waveforms[i], waveforms[j])
        DTWMatrix[j][i] = DTWMatrix[i][j]
        counter+=1
        #print("setting")



fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(DTWMatrix, cmap=plt.cm.Blues, alpha=0.3)

plt.title('Comparison Matrix', fontsize=18)
plt.show()
