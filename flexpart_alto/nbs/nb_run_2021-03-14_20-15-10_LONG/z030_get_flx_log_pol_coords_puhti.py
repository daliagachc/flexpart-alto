# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%

# %%
# this notebook was created to convert rectanfular coo


# %%
import flexpart_alto.modules.FLEXOUT as FO
import flexpart_alto.modules.flx_array as fa
from useful_scit.imps2.defs import *

# %%
log.ger.setLevel(log.log.DEBUG)

# %%
# os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
doms = ['d01', 'd02']

run_root_path = Path('/scratch/project_2001273/diego/flexpart-alto-data'
                     '/run_2021-03-14_20-15-10_LONG')

root_path = run_root_path / '*-*-*'
# root_path = '/homeappl/home/aliagadi/wrk/DONOTREMOVE
# /flexpart_management_data/runs/run_2019-06-05_18-42-11_/*-*-*'
path_out = run_root_path / 'log_pol'

run_name = 'run_2021-03-14_20-15-10_LONG'
paths = glob.glob(str(root_path))
paths.sort()

# %%
fo_base_dic = dict(
    # dom = 'd01', folder_path = '/Volumes/mbProD/Downloads/flex_out/run_2019-06
    # -02_20-42-05_/2017-12-10',
    folder_path_out=path_out,
    run_name=run_name,
)

# %%
for p in paths[:]:
    for d in doms:
        print('starting', d, p)
        new_dic = dict(dom=d, folder_path=p)
        fo_dic = {**fo_base_dic, **new_dic}

        try:
            fo = FO.FLEXOUT(**fo_dic)
            fo.export_log_polar_coords()
            print('done', d, p)
        except AssertionError as error:
            log.ger.error(error)
            print('failed when', d, p)

# %%
2

# %%
