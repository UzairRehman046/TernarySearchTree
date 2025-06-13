#!/bin/bash

#SBATCH --job-name=default_cpu_job
#SBATCH --output=default_cpu_job.out
#SBATCH --error=default_cpu_job.err

#SBATCH --partition=batch
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=3400

module load cluster/genius/amd
module load matplotlib/3.1.1-foss-2019b-Python-3.7.4

python benchmark_tst.py

