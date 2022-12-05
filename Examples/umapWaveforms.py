import numpy as np

import matplotlib.pyplot as plt
import umap

from grabRootWaveforms import openWaveforms

waveforms = openWaveforms(
    "Cherenkov",  # The keyword in the name of each waveform in the root files
    "rootWaveforms", # The directory location of all root files
    rmBackground=False # Removal of background to center background noise around 0
    )


reducer = umap.UMAP(n_neighbors=2)
embedding = reducer.fit_transform(waveforms)
#print(embedding.shape)

plt.scatter(embedding[:, 0], embedding[:, 1])
plt.title("UMAP applied to Waveforms")
for i in range(len(embedding)):
    plt.annotate(str(i), (embedding[i][0], embedding[i][1]))
plt.show()
