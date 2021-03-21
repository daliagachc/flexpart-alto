#!/bin/bash
#SBATCH -e ./error%j.txt
#SBATCH -o ./output%j.txt
#SBATCH -J flex
#SBATCH -n {SBATCH_N}
#SBATCH -t {SBATCH_T}
#SBATCH -p {SBATCH_P}
#SBATCH --mem-per-cpu={SBATCH_M}
#SBATCH --mail-type=END
#SBATCH --mail-user=diego.aliaga@helsinki.fi

# first set the environemt

module purge
module load gcc/9.1.0 intel-mkl/2019.0.4 hpcx-mpi/2.4.0 netcdf-fortran/4.4.4
export NETCDF=$(nf-config --prefix)

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME

mkdir ${{LOCAL_SCRATCH}}/data_in
ln -s ${{LOCAL_SCRATCH}}/data_in ./data_in
mkdir ${{LOCAL_SCRATCH}}/data_out
ln -s ${{LOCAL_SCRATCH}}/data_out ./data_out

flex_dir='/users/aliagadi/FLEXPART-WRF_v3.3.2-omp/'
input_flex={FLX_INPUT_PATH_TAITO}

#XX run script to load files here.


sh download_files.sh

#cd $flex_dir
#exe=flexwrf33_gnu_mpi
#exe=flexwrf33_gnu_omp
#exe=flexwrf33_gnu_serial
exe={FLX_EXE}
## run my MPI executable

cp ${{input_flex}} ./data_out/input_flex

#srun ${{flex_dir}}${{exe}} ${{input_flex}}


srun ${{flex_dir}}${{exe}} ./data_out/input_flex

swift upload {RUN_BASE_NAME}/{DAY_STR} ./data_out/
