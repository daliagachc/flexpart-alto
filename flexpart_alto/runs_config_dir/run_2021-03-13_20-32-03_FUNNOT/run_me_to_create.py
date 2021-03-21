# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

from IPython import get_ipython

# noinspection PyBroadException
try:
    _ipython = get_ipython()
    _magic = _ipython.magic
    _magic('load_ext autoreload')
    _magic('autoreload 2')
except:
    pass

# %%
import flexpart_alto.modules.daily_back.ConfigDayRun as cd
import pprint
import datetime as dt
from pathlib import Path
import flexpart_alto

# %%
run_base_name = 'run_2021-03-13_20-32-03_FUNNOT'

pack_path = Path(flexpart_alto.__path__[0])

init_dic = dict(
    DATE_START=dt.date(2018, 3, 7),
    DATE_END=dt.date(2018, 3, 7),
    HOURS_BACK_IN_TIME=96,  # possitive,
    RUN_BASE_NAME=run_base_name,
    RUN_BASE_PATH=pack_path / 'runs_config_dir',
    RUN_BASE_PATH_TAITO='/scratch/project_2001273/diego/flexpart_test_run/',
    WRFOUT_PATH='./data_in',
    FLX_INPUT_TEMPL_PATH=pack_path / 'runs_config_dir' / \
                         run_base_name / 'flex_input_templ',
    RUN_TEMPL_PATH=pack_path / 'runs_config_dir' / run_base_name / \
                   'run_flex_templ.sh',
    Z1_LEVEL=0.0,
    Z2_LEVEL=10.0,
    N_PARTICLES=20000,
    MASS_EMMITTED=1.0,
    RELEASE_NAME='alto',  # release base nameo,
    FLX_EXE='flexwrf33_gnu_omp',
    # FLX_EXE='flexwrf33_gnu_serial',
    SBATCH_N=1,
    SBATCH_T='24:00:00',
    SBATCH_P='serial',
    # SBATCH_P='parallel',
    SBATCH_M=16000,
    NUMBER_OF_RELEASES=24,
    LO_LEFT='-68.200',
    LO_RIGHT='-68.170',
    LA_TOP='-16.500',
    LA_BOTTOM='-16.520',
    BUCKET_IN='wrf_long_run',
    BUCKET_OUT='run_flx_delete',



)

pprint.pprint(init_dic)

# %%
cmd = cd.ConfigMultiDayRun(init_dic=init_dic)

# %%
# cmd.rsync_to_taito()
