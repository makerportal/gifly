#!/usr/bin/python
from mpl_toolkits.basemap import Basemap
import matplotlib
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import csv
from gifly import gif_maker
from scipy import stats

font = {'family' : 'sans-serif',
        'size'   : 26}

matplotlib.rc('font', **font)

# Grabbing the .csv data
lats,lons,capacity,year = [],[],[],[]

with open('./uswtdbCSV/uswtdb_v1_1_20180710.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        # only taking continental U.S. data and getting rid of unknown years
        if float(data['p_year'])<1950.0 or float(data['ylat'])>50 or\
        float(data['ylat'])<24 or float(data['xlong'])>-66 or\
        float(data['xlong'])<-124 or float(data['t_cap'])<0:
            continue
        
        lats.append(float(data['ylat']))
        lons.append(float(data['xlong']))
        capacity.append(float(data['t_cap']))
        year.append(float(data['p_year']))

# sorting the data based on year the turbine was built
y = np.argsort(year)
year_sort = np.array(year)[y]
lats_sort = np.array(lats)[y]
lons_sort = np.array(lons)[y]
capacity_sort = np.array(capacity)[y]

# plot and loop parameters
zoom_scale = 3
curr_year = year_sort[0]
x_array,y_array,cap_array,color_array = [],[],[],[]

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(lats_sort)-zoom_scale,np.max(lats_sort)+zoom_scale,\
        np.min(lons_sort)-zoom_scale,np.max(lons_sort)+zoom_scale]

# create the basemap for lat/lon scatter plotting
m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution=None)

# directory to be created for .png files that the GIF will need
png_dir = './png_files_size/'

# indexing for loop year
gif_indx = 0

# set capacity bounds for size interpolation
cap_min = np.min(capacity_sort)
cap_max = np.max(capacity_sort)

colormap = plt.cm.coolwarm
normalize = matplotlib.colors.Normalize(vmin = cap_min,vmax = cap_max)

loop_size = len(year_sort)
num_gifs = len(np.unique(year_sort))

for pp in range(0,loop_size):
    if year_sort[pp]==curr_year:
        x,y = m(lons_sort[pp],lats_sort[pp])
        x_array.append(x)
        y_array.append(y)
        cap_array.append(np.interp(capacity_sort[pp],[cap_min,cap_max],[30,200]))
        color_array.append(capacity_sort[pp])
        if pp!=loop_size-1:
            continue
    else:
        curr_year = year_sort[pp]

    # recreate figure each loop
    fig = plt.figure(figsize=(12,7))
    m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
                llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution=None)
    m.bluemarble() # this plots the earth-like contour to the U.S. map

    # scatter new data with the color and size changes
    scat1 = plt.scatter(x_array,y_array,s=cap_array,c = color_array,edgecolors='#444444',alpha=0.5,cmap=colormap,norm=normalize)
    plt.colorbar(scat1,label='Average Power [kW]')
    plt.ylabel(str(year_sort[pp-1])) # updated year

    gif_maker('wind_turbine_yearly_with_colors.gif',png_dir,gif_indx,num_gifs,90)
    gif_indx+=1
