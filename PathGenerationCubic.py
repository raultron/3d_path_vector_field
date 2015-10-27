from pylab import *


def path_3d(pos, loop):
    # INPUTS
    # pos: A 3xn python array with the required points of the route
    # loop: A boolean, true means that the path is cyclic i.e a loop.
    # OUPUTS
    # X, Y, Z, Tt
    # X, Y, Z: Each one a vector representing the coordinates of every point
    # in the calculated path
    # Tt: A vector with the time information associated with each point
    n_points = pos.shape[0]
    path_x = 0
    path_y = 0
    path_z = 0
    path_t = 0
    # Vector calculation for the path
    if loop:
        # If the path is a loop
        # Start and end is the same
        vectors = zeros((n_points + 1, 3))
        for i in range(n_points):
            if i < n_points - 1:
                # All the internal points
                print 'Internal point in the path:', i
                vector1 = pos[i, :] - pos[i - 1, :]
                vector2 = pos[i + 1, :] - pos[i, :]
                v_result = vector1 + vector2
                vectors[i, :] = v_result / sqrt(dot(v_result, v_result))
            else:
                # Careful with the last one
                print 'Last point in the loop:', i
                vector1 = pos[i, :] - pos[i - 1, :]
                vector2 = pos[0, :] - pos[i, :]
                v_result = vector1 + vector2
                vectors[i, :] = v_result / sqrt(dot(v_result, v_result))
        # We add an additional point to cloe the loop
        vectors[n_points, :] = vectors[0, :]
        pos = vstack((pos, pos[0]))
        n_points += 1
    else:
        # If points don't form a loop
        vectors = zeros((n_points, 3))
        for i in range(n_points):
            if (i > 0) and (i < n_points - 1):
                print 'Internal point in the path:', i
                # All the internal points
                vector1 = pos[i, :] - pos[i - 1, :]
                vector2 = pos[i + 1, :] - pos[i, :]
                v_result = vector1 + vector2
                vectors[i, :] = v_result / sqrt(dot(v_result, v_result))
            else:
                print 'The start and last point has velocity zero', i
                vectors[0, :] = zeros(3)
                vectors[n_points - 1, :] = zeros(3)

    print vectors

    to = 1
    t1 = 10
    time_step = 0.05

    for i in range(n_points - 1):
        # Initial position and velocities
        xi = pos[i, 0]
        dxi = vectors[i, 0]
        yi = pos[i, 1]
        dyi = vectors[i, 1]
        zi = pos[i, 2]
        dzi = vectors[i, 2]
        # Final position and velocities
        xf = pos[i + 1, 0]
        dxf = vectors[i + 1, 0]
        yf = pos[i + 1, 1]
        dyf = vectors[i + 1, 1]
        zf = pos[i + 1, 2]
        dzf = vectors[i + 1, 2]
        # time vector
        t = arange(to, t1, time_step)
        # Matrix for the cubic polynomial calculation
        m = array([[1, to, to ** 2, to ** 3],
                   [0, 1, 2 * to, 3 * to ** 2],
                   [1, t1, t1 ** 2, t1 ** 3],
                   [0, 1, 2 * t1, 3 * t1 ** 2]])

        A = dot(linalg.inv(m), array([[xi], [dxi], [xf], [dxf]]))
        B = dot(linalg.inv(m), array([[yi], [dyi], [yf], [dyf]]))
        C = dot(linalg.inv(m), array([[zi], [dzi], [zf], [dzf]]))

        x_temp = A[0] + A[1] * t + A[2] * t ** 2 + A[3] * t ** 3
        y_temp = B[0] + B[1] * t + B[2] * t ** 2 + B[3] * t ** 3
        z_temp = C[0] + C[1] * t + C[2] * t ** 2 + C[3] * t ** 3

        if i == 0:
            path_x = x_temp
            path_y = y_temp
            path_z = z_temp
            path_t = t
        else:
            path_x = hstack((path_x, x_temp))
            path_y = hstack((path_y, y_temp))
            path_z = hstack((path_z, z_temp))
            path_t = hstack((path_t, t))
        to += 10
        t1 += 10
    return path_x, path_y, path_z, path_t
