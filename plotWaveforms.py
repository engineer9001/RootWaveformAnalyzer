import matplotlib.pyplot as plt
import numpy as np

from grabRootWaveforms import openWaveforms

Keyword = <Root Object Keyword>
Directory = <Root File(s) Directory>

waveforms = openWaveforms(Keyword, Directory)
processedWaveforms = openWaveforms(Keyword, Directory, rmBackground=True, FFT = True)


sorted = []
for i in range(len(waveforms)):
    sorted.append(waveforms[i][:])
    sorted[i].sort()
    print(sorted[i][-3])
    plt.plot(waveforms[i])
    plt.title("Waveform #" + str(i))
    plt.savefig("Waveforms/ProcessedWaveform"+str(i)+".png")
    plt.close()

for i in range(len(processedWaveforms)):
    plt.plot(processedWaveforms[i])
    plt.title("Processed Waveform (background removed + FFT) #" + str(i))
    plt.savefig("Waveforms/ProcessedWaveform"+str(i)+".png")
    plt.close()
