#!/bin/bash -l
#SBATCH --output=array_job_out_%A_%a.txt
#SBATCH --error=array_job_err_%A_%a.txt
#SBATCH --job-name=array_job_rect_to_logpol
#SBATCH --account=project_2001273
#SBATCH --time=04:00:00
#SBATCH --partition=test
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=12000
#SBATCH --array=1,2

# run the analysis command

conda activate b3
script=/users/aliagadi/flexpart-alto/flexpart_alto/nbs/nb_run_2021-03-14_20-15-10_LONG/z035_get_flx_log_pol_coords_puhti_array.py
python ${script} ${SLURM_ARRAY_TASK_ID}