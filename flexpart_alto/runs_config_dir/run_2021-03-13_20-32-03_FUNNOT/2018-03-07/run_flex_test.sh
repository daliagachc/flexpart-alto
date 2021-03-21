#!/bin/bash
#SBATCH -e ./error%j.txt
#SBATCH -o ./output%j.txt
#SBATCH -J flex
#SBATCH -n 1
#SBATCH -t 00:30:00
#SBATCH -p test
#SBATCH --mem-per-cpu=16000
#SBATCH --mail-type=END
#SBATCH --mail-user=diego.aliaga@helsinki.fi

# first set the environemt

module purge
module load gcc/9.1.0 intel-mkl/2019.0.4 hpcx-mpi/2.4.0 netcdf-fortran/4.4.4
export NETCDF=$(nf-config --prefix)

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

mkdir ${LOCAL_SCRATCH}/data_in
ln -s ${LOCAL_SCRATCH}/data_in ./data_in
mkdir ${LOCAL_SCRATCH}/data_out
ln -s ${LOCAL_SCRATCH}/data_out ./data_out

flex_dir='/users/aliagadi/FLEXPART-WRF_v3.3.2-omp/'
input_flex=/scratch/project_2001273/diego/flexpart_test_run/run_2021-03-13_20-32-03_FUNNOT/2018-03-07/flx_input

#XX run script to load files here.


sh download_files.sh

#cd $flex_dir
#exe=flexwrf33_gnu_mpi
#exe=flexwrf33_gnu_omp
#exe=flexwrf33_gnu_serial
exe=flexwrf33_gnu_omp
## run my MPI executable

cp ${input_flex} ./data_out/input_flex

#srun ${flex_dir}${exe} ${input_flex}


srun ${flex_dir}${exe} ./data_out/input_flex

swift upload run_2021-03-13_20-32-03_FUNNOT/2018-03-07 ./data_out/
