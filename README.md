# Rainfall-Runoff-Calculator (Python)
# Project Overview:
This script calculates runoff depth based on rainfall input and a selected Curve Number. It also includes an optional visualization that illustrates the rainfall–runoff relationship commonly used in stormwater management and drainage design.

# Featured:
- Runoff estimation using SCS CN formula
- Accepts any rainfall depth (mm)
- Clean, reusable calculation function
- Optional Rainfall-Runoff Plot
- Easy to extend into larger hydrology analysis tool

# Core Function:
```
def scs_runoff(P, CN):

S=(25400 / CN)-254

Ia=0.2 * S

if P<= Ia:
 
  return 0

return ((P - Ia)**2) / (P - Ia + S)
```
# Example Usage:

```
runoff = scs_runoff(50,75)
print(f"Runoff depth: {runoff:.2f} mm")

```
# Plot Snippet

```
plt.plot(rain, runoff)
plt.xlabel("Rainfall (mm)")
plot.ylabel("Runoff (mm)")
plt.title("SCS Curve Number Runoff Response")
plt.grid(True)
plt.show()

```

# How to Run:
```
pip install numpy matplotlib
python runoff.py
python plot_runoff.py
```
# Project Structure:
📁 rainfall-runoff-calculator

│── README.md        # Project documentation

│── runoff.py        # Main SCS runoff calculator

│── plot_runoff.py   # Visualization script

│── example.png      # Optional plot image

# What I learned:
- Applying hydrology formulas into Python
- Visualizing engineering data
- Writing clear documentation
- Connecting Civil Engineering concepts with automation


