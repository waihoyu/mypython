#加图水印
from __future__ import print_function
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


datafile = cbook.get_sample_data('logo2.png', asfileobj=False)
print('loading %s' % datafile)
im = image.imread(datafile)
im[:, :, -1] = 0.5  # set the alpha channel

fig, ax = plt.subplots()

ax.plot(np.random.rand(20), '-o', ms=20, lw=2, alpha=0.7, mfc='green')
ax.grid()
fig.figimage(im, 5, 5, zorder=3)

plt.show()
