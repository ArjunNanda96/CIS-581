def edgeLink(M, Mag, Ori, low, high):
    '''
    File clarification:
        Use hysteresis to link edges based on high and low magnitude thresholds
        - Input M: H x W logical map after non-max suppression
        - Input Mag: H x W matrix represents the magnitude of gradient
        - Input Ori: H x W matrix represents the orientation of gradient
        - Input low, high: low and high thresholds 
        - Output E: H x W binary matrix represents the final canny edge detection map
    '''

    strong_map = np.multiply(M, np.greater(Mag, high))
    weak_map = np.multiply(M, np.logical_and(Mag > low, Mag <= high))

    # compute the edge direction from Ori
    edge_dir = Ori + (np.pi / 2)
    nc, nr = Ori.shape[1], Ori.shape[0]
    x, y = np.meshgrid(np.arange(nc), np.arange(nr))

    cos_map = np.cos(edge_dir) + x
    #print(np.cos(edge_dir))
    print(cos_map)
    cos_map = np.clip(x + 1, 0, nc - 1)
    print(cos_map)
    sin_map = np.sin(edge_dir)
    sin_map = np.clip(y - 1, 0, nr - 1)

    neg_edge_dir = Ori - (np.pi / 2)
    cos_map_neg = np.cos(neg_edge_dir)
    cos_map_neg = np.clip(x - 1, 0, nc - 1)
    sin_map_neg = np.sin(neg_edge_dir)
    sin_map_neg = np.clip(y + 1, 0, nr - 1) 

    xf = np.multiply(cos_map, weak_map)
    xb = np.multiply(cos_map_neg, weak_map)
    yf = np.multiply(sin_map, weak_map)
    yb = np.multiply(sin_map_neg, weak_map)

    prev_map = np.copy(strong_map)
    count = 0
    while True:
        count += 1
        N1 = interp2(strong_map, xf, yf)
        N2 = interp2(strong_map, xb, yb)
        strong_map = np.logical_or(strong_map, N1)
        strong_map = np.logical_or(strong_map, N2)
        cur_map = np.copy(strong_map)
        if np.array_equal(prev_map, cur_map):
            #print(count)
            return strong_map
        else:
            prev_map = np.copy(strong_map)
