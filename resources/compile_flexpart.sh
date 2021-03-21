#!/bin/bash
# taken from flexpart_managament project
# it was originally created by juha alto and aimed for compulation in taito
# 2021-03-11_12-56-42_:
# it does not compile in puhti. see instrucction from juha for compilation in puhti
module purge
module load gcc/7.3.0 intelmpi/18.0.2 mkl/18.0.2 hdf5-par/1.8.20 netcdf4/4.6.1

version=3.3.2
opt=mpi
opt=omp
#wget https://www.flexpart.eu/downloads/58 -O flexpart-wrf-${version}.tar.gz
tar xvf flexpart-wrf-${version}.tar.gz
mv Src_flexwrf_v${version} Src_flexwrf_v${version}-${opt}
cd Src_flexwrf_v${version}-${opt}

make -f makefile.mom $opt NETCDF=$(nc-config --prefix)
