import subprocess

import sys
from matplotlib import image as mpimg
import numpy as np
import os

nx = 200
ny = 200
nz = 1

# Generate vertices and edges
# subprocess.call(['sh', './main.sh'])

subprocess.call(["python", "write_dipha_file_3d_revise.py", "data_3d/", "inputs/complex.bin", "inputs/vert.txt"])
subprocess.call(["mpiexec", "-n", "4", "dipha-graph-recon/build/dipha", "inputs/complex.bin", "inputs/diagram.bin", "inputs/dipha.edges", "1024", "1024", "10"])
subprocess.call(["matlab", "-nodisplay", "-nojvm", "-r", "load_persistence_diagram; exit"])
subprocess.call(["src/a.out", "inputs/vert.txt", "inputs/dipha_edges.txt", "0", "output/"])

# Visualize the vertices and edges

subprocess.call(["matlab", "-nodisplay", "-nojvm", "-r", "test_process; exit"])