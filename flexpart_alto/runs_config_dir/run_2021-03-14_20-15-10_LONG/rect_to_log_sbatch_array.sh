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
script=
python ${SLURM_ARRAY_TASK_ID}