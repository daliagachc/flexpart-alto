#!/bin/bash
#SBATCH -e ./error%j.txt
#SBATCH -o ./output%j.txt
#SBATCH --account=project_2001273
#SBATCH --job-name=flex
#SBATCH --nodes={SBATCH_N}
#SBATCH --time={SBATCH_T}
#SBATCH --partition={SBATCH_P}
#SBATCH --mem-per-cpu={SBATCH_M}
#SBATCH --mail-type=END
#SBATCH --mail-user=diego.aliaga@helsinki.fi
#SBATCH --gres=nvme:400

# first set the environemt

cd {DAY_PATH_TAITO}

#module purge
module load gcc/9.1.0 intel-mkl/2019.0.4 hpcx-mpi/2.4.0 netcdf-fortran/4.4.4
export NETCDF=$(nf-config --prefix)
#module load allas

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
#allas_conf -f -k $OS_PROJECT_NAME

mkdir ${{LOCAL_SCRATCH}}/{WRFOUT_PATH}
ln -sf ${{LOCAL_SCRATCH}}/{WRFOUT_PATH} ./{WRFOUT_PATH}
mkdir ${{LOCAL_SCRATCH}}/{FLX_PATH_OUT}
ln -sf ${{LOCAL_SCRATCH}}/{FLX_PATH_OUT} ./{FLX_PATH_OUT}

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

#cp ${{input_flex}} ./{FLX_PATH_OUT}/input_flex

#srun ${{flex_dir}}${{exe}} ${{input_flex}}


#srun ${{flex_dir}}${{exe}} ./{FLX_PATH_OUT}/input_flex
srun ${{flex_dir}}${{exe}} ${{input_flex}}

cd ./{FLX_PATH_OUT}

source /appl/opt/allas-cli-utils/allas_conf -f -k $OS_PROJECT_NAME
swift upload {RUN_BASE_NAME}/{DAY_STR} ./
