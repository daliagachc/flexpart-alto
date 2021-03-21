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
"""
README:
this script will transform rect coords to logpol at puhti
it takers one artgumen: the folder where all the flexpart output resides
for that day.
example:
python z035_get_flx_log_pol_coords_puhti_array.py 2017-12-06

number of days is  of days is 177
"""
# %%
# this notebook was created to convert rectanfular coo


# %%
import flexpart_alto.modules.FLEXOUT as FO
# import flexpart_alto.modules.flx_array as fa
from useful_scit.imps2.defs import log, Path, glob
import sys

# %%
log.ger.setLevel(log.log.DEBUG)

# %%

#it starts at 1
i_to_run = int(sys.argv[1]) - 1
# i_to_run = 0

# %%
list_of_days = '''\
2017-12-06
2017-12-07
2017-12-08
2017-12-09
2017-12-10
2017-12-11
2017-12-12
2017-12-13
2017-12-14
2017-12-15
2017-12-16
2017-12-17
2017-12-18
2017-12-19
2017-12-20
2017-12-21
2017-12-22
2017-12-23
2017-12-24
2017-12-25
2017-12-26
2017-12-27
2017-12-28
2017-12-29
2017-12-30
2017-12-31
2018-01-01
2018-01-02
2018-01-03
2018-01-04
2018-01-05
2018-01-06
2018-01-07
2018-01-08
2018-01-09
2018-01-10
2018-01-11
2018-01-12
2018-01-13
2018-01-14
2018-01-15
2018-01-16
2018-01-17
2018-01-18
2018-01-19
2018-01-20
2018-01-21
2018-01-22
2018-01-23
2018-01-24
2018-01-25
2018-01-26
2018-01-27
2018-01-28
2018-01-29
2018-01-30
2018-01-31
2018-02-01
2018-02-02
2018-02-03
2018-02-04
2018-02-05
2018-02-06
2018-02-07
2018-02-08
2018-02-09
2018-02-10
2018-02-11
2018-02-12
2018-02-13
2018-02-14
2018-02-15
2018-02-16
2018-02-17
2018-02-18
2018-02-19
2018-02-20
2018-02-21
2018-02-22
2018-02-23
2018-02-24
2018-02-25
2018-02-26
2018-02-27
2018-02-28
2018-03-01
2018-03-02
2018-03-03
2018-03-04
2018-03-05
2018-03-06
2018-03-07
2018-03-08
2018-03-09
2018-03-10
2018-03-11
2018-03-12
2018-03-13
2018-03-14
2018-03-15
2018-03-16
2018-03-17
2018-03-18
2018-03-19
2018-03-20
2018-03-21
2018-03-22
2018-03-23
2018-03-24
2018-03-25
2018-03-26
2018-03-27
2018-03-28
2018-03-29
2018-03-30
2018-03-31
2018-04-01
2018-04-02
2018-04-03
2018-04-04
2018-04-05
2018-04-06
2018-04-07
2018-04-08
2018-04-09
2018-04-10
2018-04-11
2018-04-12
2018-04-13
2018-04-14
2018-04-15
2018-04-16
2018-04-17
2018-04-18
2018-04-19
2018-04-20
2018-04-21
2018-04-22
2018-04-23
2018-04-24
2018-04-25
2018-04-26
2018-04-27
2018-04-28
2018-04-29
2018-04-30
2018-05-01
2018-05-02
2018-05-03
2018-05-04
2018-05-05
2018-05-06
2018-05-07
2018-05-08
2018-05-09
2018-05-10
2018-05-11
2018-05-12
2018-05-13
2018-05-14
2018-05-15
2018-05-16
2018-05-17
2018-05-18
2018-05-19
2018-05-20
2018-05-21
2018-05-22
2018-05-23
2018-05-24
2018-05-25
2018-05-26
2018-05-27
2018-05-28
2018-05-29
2018-05-30
2018-05-31'''

list_of_days = list_of_days.split('\n')

day_to_run = list_of_days[i_to_run]

# %%

# os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

doms = ['d01', 'd02']

run_root_path = Path(
    '/scratch/project_2001273/diego/flexpart-alto-data/run_2021-03-14_20-15'
    '-10_LONG')

root_path = run_root_path / day_to_run

# root_path = '/homeappl/home/aliagadi/wrk/DONOTREMOVE
# /flexpart_management_data/runs/run_2019-06-05_18-42-11_/*-*-*'

path_out = run_root_path / 'log_pol'

log.ger.debug(f'root path is {root_path}')

run_name = 'run_2021-03-14_20-15-10_LONG'
paths = glob.glob(str(root_path))
paths.sort()

# %%
fo_base_dic = dict(
    # dom = 'd01', folder_path = '/Volumes/mbProD/Downloads/flex_out/run_2019
    # -06-02_20-42-05_/2017-12-10',
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


# %%
