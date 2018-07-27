# gifly

This module is dedicated to creating GIFs for data visualization. If used in a loop, it saves the user's plot as a .png file in a nearby folder, then at the end of the loop takes those .png files and creates an animation in .gif format.

The user should use 'from gifly import gif_maker' at the header of their script. Then use the function accordingly:

######

gif_maker(gif_name,png_dir,gif_indx,num_gifs,dpi)

######

gif_name == name of the GIF once it is created

png_dir == name of the .png directory to save the files

gif_indx == current index in the GIF loop (must be a number, which will then be used to collate and create animation)

num_gifs == total number of .png files to be used in the GIF.

dpi == size of each .png file to be save and used in the creation of the GIF.

<img src="https://github.com/engineersportal/gifly/blob/master/wind_turbine_dist.gif"/>
