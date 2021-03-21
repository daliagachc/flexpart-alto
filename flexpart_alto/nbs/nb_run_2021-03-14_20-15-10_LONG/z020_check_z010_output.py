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
# this notebook was created to convert rectanfular coo

# %load_ext autoreload
# %autoreload 2

# %%
import flexpart_alto.modules.FLEXOUT as FO
import flexpart_alto.modules.flx_array as fa
import flexpart_alto.modules.constants as co
from useful_scit.imps2.defs import *

# %%
p1 = \
'/Volumes/Transcend/diego_tr/flexpart-alto/flexpart_alto/data_small/d_run_2021-03-14_20-15-10_LONG/log_pol/run_2021-03-14_20-15-10_LONG/d01_2018-01-06_00-00-00.nc'

# %%
ds = xr.open_dataset(p1)

# %%
d1 = ds.reset_coords()[['LAT','LON']].to_dataframe()

# %%
d1['a'] = 0

# %%
d1.plot(x='LON',y='LAT')

# %%
plt.rcParams['figure.dpi'] = 600
ds[{co.RL:12}]['CONC'].plot(x='LON',y='LAT',norm=mpl.colors.LogNorm(vmin=1,vmax=10000))

# %%
