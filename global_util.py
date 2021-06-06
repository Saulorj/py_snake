
RUNNING, PAUSE, END = 0, 1, 2
frame_rate = 30
border = 5
matrix = (25, 25)
square_size = 25

color_white = (255,255,255)
color_black = (0,0,0)
color_grey = (166, 165, 162)
color_green = (0,255,0)
color_red = (255,0,0)

def convert_matrix_game_area(x, y, game_area):
    x_area = game_area[0] + (x * square_size)
    y_area = game_area[1] + (y * square_size)
    return x_area, y_area
