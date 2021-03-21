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

# %% [markdown]
# # imports

# %%
from useful_scit.imps2.defs import *

# %%
from skimage.util.shape import view_as_windows as viewW


def strided_indexing_roll(a, r):
    # Concatenate with sliced to cover all rolls
    
    assert a.shape[0]==r.shape[0], 'roll vector does not match matrix shape'
    p = np.full((a.shape[0],a.shape[1]-1),np.nan)
    a_ext = np.concatenate((p,a,p),axis=1)

    # Get sliding windows; use advanced-indexing to select appropriate ones
    n = a.shape[1]
    return viewW(a_ext,(1,n))[np.arange(len(r)), -r + (n-1),0]


# %% [markdown]
# # example

# %%

# %%
a  = np.array([
    [ 1, 2, 3],
    [ 1, 2, 3],
    [11,22,33],
    [21,22,23]
    
])

r = np.array([1,2,3,4])

# %%
strided_indexing_roll(a,r)

# %%
viewW(a_ext,(1,5))[0]

# %%
a.shape[1]==r.shape[0]


# %%
# %load_ext memory_profiler

# %% [markdown]
# # flx example

# %%
def f1():
    f = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/flxout_d02_20171217_000000.nc'
    d = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/header_d02.nc'

    ds = xr.open_dataset(f)
    hs = xr.open_dataset(d)

    to = hs['TOPOGRAPHY']

    shifts = np.round(to/500).astype(int)

    co = ds['CONC']
    co = co[{'Time':0,'releases':0,'ageclass':0}]


#     co.sum('south_north').plot()

    c1 = co.stack({'sw':['south_north','west_east']})
    s1 = shifts.stack({'sw':['south_north','west_east']})

    c1d = c1.values
    s1d = s1.values

    res = strided_indexing_roll(c1d.T,s1d).T

    c1d.shape,res.shape

    c2 = xr.full_like(c1,0.0) + res

    c3 = c2.unstack()

    c4 = c3.sum('south_north') - co.sum('south_north')
#     c4.plot()
    return c4 
    
    

#     c4.plot.contour()



# %%
# doesnt work 
def f2():
    f = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/flxout_d02_20171217_000000.nc'
    d = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/header_d02.nc'

    ds = xr.open_dataset(f)
    hs = xr.open_dataset(d)

    to = hs['TOPOGRAPHY']

    shifts = np.floor(to/500).astype(int)

    co = ds['CONC']
    co = co[{'Time':slice(0,10),'releases':0,'ageclass':0}]


#     co.sum('south_north').plot()
    sdim = ['south_north','west_east','Time']
    c1 = co.stack({'sw':sdim})
    s1 = shifts.stack({'sw':sdim})

    c1d = c1.values
    s1d = s1.values

    res = strided_indexing_roll(c1d.T,s1d).T

    c1d.shape,res.shape

    c2 = xr.full_like(c1,0.0) + res

    c3 = c2.unstack()

#     c4 = c3.sum('south_north') - co.sum('south_north')
#     c4.plot()
    return c4 

# %%
# %load_ext line_profiler

# %%
# # %timeit c4 = f1()
# %lprun -f f1 c4 = f1()
# c4.plot()


# %% [markdown]
# # from previous

# %%
from flexpart_alto.modules import constants as co


# %%
def from_agl_to_asl(
        ds ,
        ds_var='conc_norm' ,
        delta_z=500 ,
        z_top=15000 ,
        ds_var_name_out=None
        ) :
    log.ger.warning(
        f'this will only work if ds z levels are constant' )
    import wrf
    
    t_list = [ co.ZM , co.R_CENTER , co.TH_CENTER ]
    d3d = ds[ ds_var ]  # .sum( [ co.RL ] )
    d3d_attrs = d3d.attrs
    d3d = d3d.transpose(
        co.RL , *t_list , transpose_coords=True
        )
    dz = d3d[ co.TOPO ] + np.round( d3d[ co.ZM ] / delta_z ) * delta_z
    d3d = d3d.reset_coords( drop=True )
    dz = dz.transpose( *t_list , transpose_coords=True )
    dz = dz.reset_coords( drop=True )
    # %%
    # print( d3d.shape )
    # print( dz.shape )
    # %%
    z_lev = np.arange( delta_z / 2 , z_top , delta_z )
    da_interp = wrf.interplevel( d3d , dz , z_lev )
    da_reinterp = da_interp.rename( level=co.ZM )

    # %%
    ds_chop = ds.isel( { co.ZM : slice( 0 , len( da_reinterp[ co.ZM ] ) ) } )
    for coord in list( ds.coords ) :
        da_reinterp = da_reinterp.assign_coords(
            **{ coord : ds_chop[ coord ] } )
    if ds_var_name_out is not None :
        da_reinterp.name = ds_var_name_out

    # we do this in order to avoid the problem of setting attributes
    # to none that cannot be saved using to netcdf.
    da_reinterp.attrs = d3d_attrs

    ds_reinterp = da_reinterp.to_dataset()
    # todo: check that concentrations are the same after resampling
    return ds_reinterp


# %%
f = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/flxout_d02_20171217_000000.nc'
d = '/Users/diego/flexpart_management/flexpart_management/notebooks/log_pol_revisited/data/header_d02.nc'

ds = xr.open_dataset(f)
hs = xr.open_dataset(d)

# %%
ds

# %%
