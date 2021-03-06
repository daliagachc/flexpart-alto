# taken from project name: flexpart_management
# created by diego aliaga daliaga_at_chacaltaya.edu.bo
import cartopy
import numpy as np
import os

import flexpart_alto
from useful_scit import plot as ucp

_fm_path = flexpart_alto.__file__
fm_path = os.path.dirname(_fm_path)

PUHTI_DATA = '/scratch/project_2001273/diego/flexpart-alto-data'

PROJ = cartopy.crs.PlateCarree()
TIME = 'Time'
AC = 'ageclass'
TH = 'Time_h'
WE = 'west_east'
SN = 'south_north'
TOPO = 'TOPOGRAPHY'
ZM = 'ZMID'
ZB = 'ZBOT'
ZT = 'ZTOP'
ZLM = 'ZLEN_M'
ALT = 'ALT'
BT = 'bottom_top'
RL = 'releases'
VOL = 'VOL'
GA = 'GRIDAREA'
CONC = 'CONC'
LAT = 'LAT'
LON = 'LON'
LL_DIS = 'LL_DIS'
LL_ANG = 'LL_ANG'
ACTUAL_TIME = 'ACTUAL_TIME'
R_CENTER = 'R_CENTER'
TH_CENTER = 'TH_CENTER'
LAT_00 = 'LAT_00'
LAT_10 = 'LAT_10'
LAT_11 = 'LAT_11'
LAT_01 = 'LAT_01'
LON_00 = 'LON_00'
LON_10 = 'LON_10'
LON_11 = 'LON_11'
LON_01 = 'LON_01'

# todo: change the follwing 2 to alto center
CHC_LAT_ = -16.350427
CHC_LON_ = -68.131335
ALT_LAT = -16.509722
ALT_LON = -68.187445
LPB_LAT = -16.507125
LPB_LON = -68.129299
ORI_LAT = -16.509722
ORI_LON = -68.187445

LL00 = [LAT_00,
        LAT_10,
        LAT_11,
        LAT_01,
        LON_00,
        LON_10,
        LON_11,
        LON_01, ]

ROUND_R_LOG = .18
ROUND_TH_RAD = np.pi / 18

CPer = 'CONC_per'
CC = 'CONC_conc'
CCPer = 'CONC_conc_per'
ClusFlag = 'flags'
LAB = 'lab'

COL = 'CON_TIME/LEN'

LOLA_LAPAZ = [-70, -66, -18, -14]
LOLA_BOL = [-83, -43, -35, 2]

print('reload')

FLAGS = 'flags'
H = 'H'

PLOT_LABS = {
    CPer: 'mass*res. time[%]',
    H: 'height [masl]',
    ZM: 'height [mag]',
    CONC: 'mass/mass * res. time [s]',
    CC: 'mass/(mass * res. time * vol) [s/m3]',
}

CLUS_LENGTH_DIM = 'CLUS_LENGTH_DIM'
CONC_NORMALIZED = 'CONC_NORMALIZED'
CONC_NORMS = 'CONC_NORMS'
DUM_STACK = 'dum'
FLAG = 'FLAG'
KMEAN_OBJ = 'KMEAN_LAB'
LAB_CLUSTER_THRESHOLD = 'LAB_CLUSTER_THRESHOLD'
SIL_SC = "SIL_SCORE"
SIL_SAMPLE = "SIL_SAMPLE"
DIS = 'Distance CHC [km]'
AGECLASS = 'ageclass'
SPECIES = 'species'
RECEPTORS = 'receptors'

XLONG_CORNER = 'XLONG_CORNER'
XLAT_CORNER = 'XLAT_CORNER'
ZTOP = 'ZTOP'
# AGECLASS = 'ageclass'
RELEASENAME = 'ReleaseName'
RELEASETSTART_END = 'ReleaseTstart_end'
RELEASEXSTART_END = 'ReleaseXstart_end'
RELEASEYSTART_END = 'ReleaseYstart_end'
RELEASEZSTART_END = 'ReleaseZstart_end'
RELEASENP = 'ReleaseNP'
TOPOGRAPHY = 'TOPOGRAPHY'
GRIDAREA = 'GRIDAREA'
RELEASE_TIME = 'RELEASE_TIME'
WEST_EAST = 'west_east'
SOUTH_NORTH = 'south_north'
XLONG = 'XLONG'
XLAT = 'XLAT'

VLONG = 'VLONG'
VLAT = 'VLAT'

D1 = 'd01'

D2 = 'd02'

HEAD_VARS = [
    XLONG_CORNER,
    XLAT_CORNER,
    ZTOP,
    AGECLASS,
    RELEASENAME,
    RELEASETSTART_END,
    RELEASEXSTART_END,
    RELEASEYSTART_END,
    RELEASEZSTART_END,
    RELEASENP,
    TOPOGRAPHY,
    GRIDAREA,
]

CSUM = 'CONC_SUM'

RAD_MIN = 00.07
"""minimum radial distance to consider in the algorithm"""
RAD_MAX = 20.00
"""maximum radial distance to consider in the algorithm """

above_thre_label = 'above_thre'
CONC_SMOOTH_NORM = 'conc_smooth_norm'
short_range_clusters = [13, 17, 3, 2, 11, 16]
short_range_clusters.sort()
mid_short_range_clusters = [5, 10, 6, 12]
mid_short_range_clusters.sort()
mid_range_clusters = [15, 1, 14, 7, 8]
mid_range_clusters.sort()
long_range_clusters = [9, 0, 4]
long_range_clusters.sort()
# tmp_data_path = os.path.join(fm_path,'tmp_data')

# latest_ds_mac = os.path.join(tmp_data_path,'ds_clustered_18_conc_smooth.nc')
# prop_df_path = os.path.join(tmp_data_path, 'prop_df_.csv')

# silhouette_path = os.path.join(tmp_data_path,'silhouette_scores.pickle')
# %%


# %%
paper_fig_path = '/Users/diego/wrf-flexpart-chc/src/figures'

# %%
import seaborn as sns

pathway_colors = sns.color_palette('Dark2', 6)
pw_col_dict = {
    '03_PW': pathway_colors[5],
    '05_PW': pathway_colors[2],
    '07_PW': pathway_colors[4],
    '08_PW': pathway_colors[1],
    '11_PW': pathway_colors[3],
    '12_PW': pathway_colors[0],
}
import pandas as pd

# def get_nc18_order():
#     _d = {'SR': 0, 'SM': 1, 'MR': 2, 'LR': 3}
#     dic_186: pd.DataFrame = pd.read_csv(
#         os.path.join(tmp_data_path, 'nc_18_nc_06.csv'))
# dic_186['range'] = dic_186['18_NC'].str[-2:]
# dic_186['sr'] = dic_186['range'].apply(lambda v: _d[v])
# dic_186 = dic_186.sort_values(['06_NC', 'sr'])
# return dic_186
# DIC_186 = get_nc18_order()

lola_la_paz_pol = np.array([
    [-68.14983926709843, -16.44601858277946],
    [-68.17676401130821, -16.45842747012333],
    [-68.20699332725594, -16.46782119631241],
    [-68.24167170603454, -16.47410357175557],
    [-68.24906801943689, -16.49578333092283],
    [-68.2421061926304, -16.53406889758957],
    [-68.22380596334916, -16.57122890126927],
    [-68.19937778613702, -16.58332554661375],
    [-68.17754194395538, -16.56286465541125],
    [-68.15877990042677, -16.55043445826305],
    [-68.11750904879429, -16.55351421988867],
    [-68.0751159107846, -16.55664250407942],
    [-68.03790936355738, -16.55266957965353],
    [-68.02994726404417, -16.53406305600426],
    [-68.07161656278039, -16.50234397112687],
    [-68.06094935027797, -16.47038072490646],
    [-68.09486836586018, -16.47841751974281],
    [-68.09868031543392, -16.46686834999942],
    [-68.08180094405442, -16.44646771623007],
    [-68.11040248277776, -16.45416102691552],
    [-68.1260875449223, -16.46500293898034],
    [-68.14162841046189, -16.45847034995099],
    [-68.14983926709843, -16.44601858277946],
]
)

_range_colors = dict(
    SR=ucp.cc[0],
    SM=ucp.cc[1],
    MR=ucp.cc[2],
    LR=ucp.cc[3]
)

range_colors_ser = pd.Series(_range_colors)

_range_markers = dict(
    SR='o',
    SM='s',
    MR='^',
    LR='p'
)
range_markers_ser = pd.Series(_range_markers)
