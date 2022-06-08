def check_if_next_is_road(x=[[False, False, False, False], [False, False, False, False]], initial_loc=(0, 0)):
    """
    from initial location
    go 1 step up
    check if it is road, if it is then return tuple(initial_x,initial_y-1)
    if it is false then check 1 step right, if it is true then return tuple(initial_x+1,initial_y)
    if it is false then check 1 step down, if it is true then return tuple(initial_x,initial_y+1)
    if it is false then check 1 step left, it it is true then return tuple(initial_x-1,initial_y)
    """
    i, j = initial_loc[0], initial_loc[1]
    if x[i][j]:
        if len(x) > i + 1 and x[i + 1][j]:
            return (i + 1, j), True
        elif len(x[1]) > j + 1 and x[i][j + 1]:
            return (i, j + 1), True
    return initial_loc, False


def route_planner(m, a=[0, 0, 2, 2]):
    """

    :param m:
    :param a: to control when to stop the
    :return:
    """
    init_locate = (a[0], a[1])
    status = True
    while status and (init_locate[0] < a[2] or init_locate[1] < a[3]):
        init_locate, status = check_if_next_is_road(x=m, initial_loc=init_locate)
        print(F'loc {init_locate} status {status}')
