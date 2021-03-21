#!/bin/bash
#SBATCH -e ./error%j.txt
#SBATCH -o ./output%j.txt
#SBATCH --account=project_2001273
#SBATCH --job-name=flex
#SBATCH --nodes=1
#SBATCH --time=24:00:00
#SBATCH --partition=small
#SBATCH --mem-per-cpu=16000
#SBATCH --mail-type=END
#SBATCH --mail-user=diego.aliaga@helsinki.fi
#SBATCH --gres=nvme:400

# first set the environemt

cd /scratch/project_2001273/diego/flexpart_test_run/run_2021-03-14_20-15-10_LONG/2018-01-06

#module purge
module load gcc/9.1.0 intel-mkl/2019.0.4 hpcx-mpi/2.4.0 netcdf-fortran/4.4.4
export NETCDF=$(nf-config --prefix)
#module load allas

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
#allas_conf -f -k $OS_PROJECT_NAME

mkdir ${LOCAL_SCRATCH}/./data_in
ln -sf ${LOCAL_SCRATCH}/./data_in ././data_in
mkdir ${LOCAL_SCRATCH}/./data_out
ln -sf ${LOCAL_SCRATCH}/./data_out ././data_out

flex_dir='/users/aliagadi/FLEXPART-WRF_v3.3.2-omp/'
input_flex=/scratch/project_2001273/diego/flexpart_test_run/run_2021-03-14_20-15-10_LONG/2018-01-06/flx_input

#XX run script to load files here.


sh download_files.sh

#cd $flex_dir
#exe=flexwrf33_gnu_mpi
#exe=flexwrf33_gnu_omp
#exe=flexwrf33_gnu_serial
exe=flexwrf33_gnu_omp
## run my MPI executable

#cp ${input_flex} ././data_out/input_flex

#srun ${flex_dir}${exe} ${input_flex}


#srun ${flex_dir}${exe} ././data_out/input_flex
srun ${flex_dir}${exe} ${input_flex}

cd ././data_out

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
swift upload run_2021-03-14_20-15-10_LONG/2018-01-06 ./
