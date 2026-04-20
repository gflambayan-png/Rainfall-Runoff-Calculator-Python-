import numpy as np
import matplotlib.pyplot as plt
from runoff import scs_runoff

#Settings
CN=75
rain=np.linspace(0,150,300)

#Calculate runoff
runoff=[scs_runoff(p, CN) for p in rain]

#Plot
plt.plot(rain, runoff, label=f'CN={CN}')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Runoff (mm)')
plt.title('SCS Curve Number Runoff Response')
plt.grid(True)
plt.legend()
plt.show()