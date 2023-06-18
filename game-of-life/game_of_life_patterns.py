from constants import CELL_ACTIVE, CELL_INACTIVE, GRID_WIDTH, GRID_HEIGHT


def get_gun_one_state():
    """Set the initial state to the gun one state"""
    print("get_gun_one_state")
    gun_one_grid = [
        [CELL_INACTIVE for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)
    ]
    gun_one_grid[5][1] = CELL_ACTIVE
    gun_one_grid[5][2] = CELL_ACTIVE
    gun_one_grid[6][1] = CELL_ACTIVE
    gun_one_grid[6][2] = CELL_ACTIVE

    gun_one_grid[5][11] = CELL_ACTIVE
    gun_one_grid[6][11] = CELL_ACTIVE
    gun_one_grid[7][11] = CELL_ACTIVE

    gun_one_grid[4][12] = CELL_ACTIVE
    gun_one_grid[8][12] = CELL_ACTIVE

    gun_one_grid[3][13] = CELL_ACTIVE
    gun_one_grid[9][13] = CELL_ACTIVE

    gun_one_grid[3][14] = CELL_ACTIVE
    gun_one_grid[9][14] = CELL_ACTIVE

    gun_one_grid[6][15] = CELL_ACTIVE

    gun_one_grid[4][16] = CELL_ACTIVE
    gun_one_grid[8][16] = CELL_ACTIVE

    gun_one_grid[5][17] = CELL_ACTIVE
    gun_one_grid[6][17] = CELL_ACTIVE
    gun_one_grid[7][17] = CELL_ACTIVE

    gun_one_grid[6][18] = CELL_ACTIVE

    gun_one_grid[3][21] = CELL_ACTIVE
    gun_one_grid[4][21] = CELL_ACTIVE
    gun_one_grid[5][21] = CELL_ACTIVE

    gun_one_grid[3][22] = CELL_ACTIVE
    gun_one_grid[4][22] = CELL_ACTIVE
    gun_one_grid[5][22] = CELL_ACTIVE

    gun_one_grid[2][23] = CELL_ACTIVE
    gun_one_grid[6][23] = CELL_ACTIVE

    gun_one_grid[1][25] = CELL_ACTIVE
    gun_one_grid[2][25] = CELL_ACTIVE
    gun_one_grid[6][25] = CELL_ACTIVE
    gun_one_grid[7][25] = CELL_ACTIVE

    gun_one_grid[3][35] = CELL_ACTIVE
    gun_one_grid[4][35] = CELL_ACTIVE

    gun_one_grid[3][36] = CELL_ACTIVE
    gun_one_grid[4][36] = CELL_ACTIVE
    return gun_one_grid


def get_gun_two_state():
    """Set the initial state to the gun two state"""
    print("get_gun_two_state")
    gun_two_grid = [
        [CELL_INACTIVE for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)
    ]
    gun_two_grid[1][5] = CELL_ACTIVE
    gun_two_grid[2][5] = CELL_ACTIVE
    gun_two_grid[1][6] = CELL_ACTIVE
    gun_two_grid[2][6] = CELL_ACTIVE

    gun_two_grid[11][5] = CELL_ACTIVE
    gun_two_grid[11][6] = CELL_ACTIVE
    gun_two_grid[11][7] = CELL_ACTIVE

    gun_two_grid[12][4] = CELL_ACTIVE
    gun_two_grid[12][8] = CELL_ACTIVE

    gun_two_grid[13][3] = CELL_ACTIVE
    gun_two_grid[13][9] = CELL_ACTIVE

    gun_two_grid[14][3] = CELL_ACTIVE
    gun_two_grid[14][9] = CELL_ACTIVE

    gun_two_grid[15][6] = CELL_ACTIVE

    gun_two_grid[16][4] = CELL_ACTIVE
    gun_two_grid[16][8] = CELL_ACTIVE

    gun_two_grid[17][5] = CELL_ACTIVE
    gun_two_grid[17][6] = CELL_ACTIVE
    gun_two_grid[17][7] = CELL_ACTIVE

    gun_two_grid[18][6] = CELL_ACTIVE

    gun_two_grid[21][3] = CELL_ACTIVE
    gun_two_grid[21][4] = CELL_ACTIVE
    gun_two_grid[21][5] = CELL_ACTIVE

    gun_two_grid[22][3] = CELL_ACTIVE
    gun_two_grid[22][4] = CELL_ACTIVE
    gun_two_grid[22][5] = CELL_ACTIVE

    gun_two_grid[23][2] = CELL_ACTIVE
    gun_two_grid[23][6] = CELL_ACTIVE

    gun_two_grid[25][1] = CELL_ACTIVE
    gun_two_grid[25][2] = CELL_ACTIVE
    gun_two_grid[25][6] = CELL_ACTIVE
    gun_two_grid[25][7] = CELL_ACTIVE

    gun_two_grid[35][3] = CELL_ACTIVE
    gun_two_grid[35][4] = CELL_ACTIVE

    gun_two_grid[36][3] = CELL_ACTIVE
    gun_two_grid[36][4] = CELL_ACTIVE
    return gun_two_grid
