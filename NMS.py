from numpy.lib.function_base import interp
def nonMaxSup(Mag, Ori):
    '''
    File clarification:
        Find local maximum edge pixel using NMS along the line of the gradient
        - Input Mag: H x W matrix represents the magnitude of derivatives
        - Input Ori: H x W matrix represents the orientation of derivatives
        - Output M: H x W binary matrix represents the edge map after non-maximum suppression
    '''
    """
    nc, nr = Ori.shape[1], Ori.shape[0]
    x, y = np.meshgrid(np.arange(nc), np.arange(nr))
    
    y_down = np.clip(y + 1, 0, nr - 1) 
    y_up = np.clip(y - 1, 0, nr - 1)
    x_right = np.clip(x + 1, 0, nc - 1)
    x_left = np.clip(x - 1, 0, nc - 1)

    cos_map = np.cos(Ori) + x_right
    sin_map = np.sin(Ori) + y_up

    neg_Ori = Ori + np.pi
    cos_map_neg = np.cos(neg_Ori) + x_left
    sin_map_neg = np.sin(neg_Ori) + y_down

    # using interpolation to get neighbor


    #check to see if they are in bounds
    neighbor1 = interp2(Mag, cos_map, sin_map)
    neighbor2 = interp2(Mag, cos_map_neg, sin_map_neg)
    print(neighbor1)
    print(neighbor2)

    # getting neighbor in the opposite of the oritention direction
    
    binary_map = np.logical_and(Mag >= neighbor1, Mag >= neighbor2)
    return binary_map
    """
    nc, nr = Ori.shape[1], Ori.shape[0]
    x, y = np.meshgrid(np.arange(nc), np.arange(nr))
    
    y_down = np.clip(y + 1, 0, nr - 1) 
    y_up = np.clip(y - 1, 0, nr - 1)
    x_right = np.clip(x + 1, 0, nc - 1)
    x_left = np.clip(x - 1, 0, nc - 1)

    cos_map = np.cos(Ori) + x
    print(cos_map)
    cos_map_oob = np.logical_and(np.around(cos_map, 5) >= 0, cos_map <= (nc - 1))
    sin_map = np.sin(Ori) + y
    print(sin_map)
    sin_map_oob = np.logical_and(np.around(sin_map, 5) >= 0, sin_map <= (nr - 1))
    forward_oob = np.logical_and(sin_map_oob, cos_map_oob)
    neighbor1 = interp2(Mag, cos_map, sin_map)
    print(neighbor1)
    N1_trim = np.multiply(neighbor1, forward_oob)
    print(N1_trim)

    cos_map_neg = np.cos(Ori + np.pi) + x
    cos_map_neg_oob = np.logical_and(np.around(cos_map_neg, 5) >= 0, cos_map_neg <= (nc - 1))
    sin_map_neg = np.sin(Ori + np.pi) + y
    sin_map_neg_oob = np.logical_and(np.around(sin_map_neg, 5) >= 0, sin_map_neg <= (nr - 1))
    backwards_oob = np.logical_and(sin_map_neg_oob, cos_map_neg_oob)
    neighbor2 = interp2(Mag, cos_map_neg, sin_map_neg)
    N2_trim = np.multiply(neighbor2, backwards_oob)

    #print(N1_trim)
    #print(N2_trim)

    binary_map = np.logical_and(Mag >= N1_trim, Mag >= N2_trim)
    return binary_map
