# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.0-rc1
#   kernelspec:
#     display_name: Python [conda env:b36]
#     language: python
#     name: conda-env-b36-py
# ---

# %%
"""
this is a test script used locally to test if de logpolar conversion

"""
# %%
# this notebook was created to convert rectanfular coo

# %load_ext autoreload
# %autoreload 2

# %%
import flexpart_alto.modules.FLEXOUT as FO
import flexpart_alto.modules.flx_array as fa
from useful_scit.imps2.defs import *

# %%
log.ger.setLevel(log.log.DEBUG)

# %%
# os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
doms = [
    'd01',
    # 'd02',
]
root_path = '/Volumes/Transcend/diego_tr/flexpart-alto/flexpart_alto/data_small/d_run_2021-03-14_20-15-10_LONG/*-*-*'
# root_path = '/homeappl/home/aliagadi/wrk/DONOTREMOVE/flexpart_management_data/runs/run_2019-06-05_18-42-11_/*-*-*'
path_out = '/Volumes/Transcend/diego_tr/flexpart-alto/flexpart_alto/data_small/d_run_2021-03-14_20-15-10_LONG/log_pol'

run_name = 'run_2021-03-14_20-15-10_LONG'
paths = glob.glob(root_path)
paths.sort()

# %%
paths

# %%
fo_base_dic = dict(
    # dom = 'd01',
    # folder_path = '/Volumes/mbProD/Downloads/flex_out/run_2019-06-02_20-42-05_/2017-12-10',
    folder_path_out=path_out,
    run_name=run_name,
)

# %%
for p in paths:
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
