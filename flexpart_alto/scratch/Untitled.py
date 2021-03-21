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
from useful_scit.imps2.defs import *

# %%
path = '../resources/wrf-flexpart-required-fields.xlsx'

# %%
df = pd.read_excel(path)

# %%
b = df['used'] == 1
df1 = df[b]

# %%
df1.head()

# %%
wrf_path = '/Volumes/Transcend/Downloads/wrfout_d01_2017-12-21_20:00:00'
ds = xr.open_dataset(wrf_path)

# %%
WF = 'WRF variable'
va = df1[WF].values

# %%
for v in var:
    ds[va]

# %%
ds1 = ds[va]

# %%
za.compressed_netcdf_save(ds1,'/tmp/w0.nc',complevel=4)
za.compressed_netcdf_save(ds,'/tmp/wF.nc')

# %%
45/70

# %%
    
