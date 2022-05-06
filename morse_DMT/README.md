### Step 1 - generate dipha file

write_dipha_file_3d.py

takes path to image stack, output complex filename, and output vert filename

an example command:

> python write_dipha_file_3d_revise.py data_2d/ inputs/complex.bin inputs/vert.txt


### Step 2 - run dipha

%% You only need to run cmake & make once

(dipha-graph-recon folder

run the following commands in this folder to build dipha

rm -rf build/ (this removes my build directory)

mkdir build

cd build

cmake ..

make)

now that dipha is built, you can run

you need the number of processes you will use, path to complex file, path to diagram output, path to dipha edges output, and dimensions of your data - this will be the final line printed to console when running write_dipha_file_3d.py.

an example command:

mpiexec -n 4 dipha-graph-recon/build/dipha inputs/complex.bin inputs/diagram.bin inputs/dipha.edges 1137 855 270

If you do not need distributed computing, leave off the mpiexec -n 32 portion of the command

In the above example:

32 represents the number of processes used, change this to be appropriate for you machine

dipha/inputs/new_stp_2/complex.bin the input file generated in step 1!

dipha/inputs/new_stp_2/diagram.bin will be where diagram gets outputted - you will not need this file

dipha/inputs/new_stp_2/dipha.edges will be where edge file gets outputted -- you will need this file

1137 855 270 are the dimensions

### Step 3 - convert dipha output from binary

load_persistence_diagram.m

takes two arguments

first - dipha.edges file generated in step 2

second - path to output file that is a .txt version of the input file.  our morse framework takes this as input

an example command: 

load_persistence_diagram('inputs/dipha.edges','inputs/dipha_edges.txt')

### Step 4 - run discrete morse graph reconstruction

src folder

to build, enter the following command

%% You only need to compile once

(g++ ComputeGraphReconstruction.cpp)

4 inputs:

first is the vert.txt file generated in step 1

second is the dipha_edges.txt file generated in step 3

third is the persistence threshold - you get to choose! the higher the number the less number of edges will be in the output

fourth is the output folder, which will output a vert file and a edge file - this graph is the morse output

an example command:

src/a.out inputs/vert.txt inputs/dipha_edges.txt 0 output/

### All you need to do is to run the 'main.py' file!

You need to change the size of the data to adapt your owm data:

1) main.py: subprocess.call(["mpiexec", "-n", "4", "dipha-graph-recon/build/dipha", "inputs/complex.bin", "inputs/diagram.bin", "inputs/dipha.edges", "1024", "1024", "10"])

(1024, 1024, 10) is the data size. the format will be (xx, xx, 1) for 2D data.

2) visualize: mask = zeros(1024,1024,10);

(1024, 1024, 10) is the data size. the format will be (xx, xx) for 2D data.

