# 3d_path_vector_field
This repository contains python helper files which allows the calculation and display of 3D paths and vector fields for using in robot path following.

Requirenments:

Tested in Ubuntu 12.04 and 14.04 with Python 2.7

Installation and usage:

1 - Install Mayavi (Scientific visualization package for 2D and 3D data)
sudo apt-get install mayavi2

2- Clone the repo and execute the file "FieldGeneration.py". If everything is working you should see a Mayavi windows with a visualization of the Path, the 3D vector field and the streamlines.

The function path_3d(pos, loop) included in the file "PathGenerationCubic.py" takes as an argument an array of 3D points (pos) where the path should pass and boolean (loop) which defines if the trayectory is closed or open. The return of the function is an array for each coordinate of the path and the time (path_x, path_y, path_z and path_t).

The file "FieldGeneration.py" uses this function to generate a path and then it calculates an aproximation vector to the path for each point inside a cube, using a methodology of vector navigation that is described for 2D paths in paper: TODO. This script then uses matplotlib to show the resulting path and the striplines to observe the possible paths from every point in space.

If you wan to create you own paths you only have to modify "FieldGeneration.py". For example, to define 3 points in a closed loop configuration:

Pos0 = array([4, 8, 3])
Pos1 = array([14, 12, 17])
Pos2 = array([14, 4, 17])
Loop = True
Pos = array([Pos0, Pos1, Pos2])

path_x, path_y, path_z, path_t = path_3d(Pos, Loop)

and then:

vector_field_3D, Xc, Yc, Zc = calc_vec_field_fast(X, Y, Z, 20, 1)


To create a different path it is only necessary to modify

