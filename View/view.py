"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/PG Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame as PG 
from CSPSolver.CSPSolver import CSPSolver


grid = []

# Define some colors
black = (0, 0, 0)
lightgreen = (202,255,112)
brown = (184,134,11)
white = (245, 245, 245)
purple = (147,112,219)
green = (0,128,0)
yellow = (238,238,0)
pink = (255,182,193)
violet = (199,21,133)
red = (205,0,0)
grey = (193,205,205)
cyan = (0,205,205)
blue = (16,78,139)

map_color_to_id = {
    "black": 1,
    "lightgreen": 2,
    "brown": 3,
    "white": 4,
    "purple": 5,
    "green": 6,
    "yellow": 7,
    "pink": 8,
    "violet": 9,
    "cyan": 10,
    "red": 11,
    "blue": 12
}

map_id_to_color = {
    0: white,
    1: black,
    2: lightgreen,
    3: brown,
    4: white,
    5: purple,
    6: green,
    7: yellow,
    8: pink,
    9: violet,
    10: cyan,
    11: red,
    12: blue
}


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
COLUMN = 9
ROW = 11

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
# draw as black box some cells such that final grid contains only diagonal cells

def drawCurrentShape(shape): 
    for coords in shape[0]:
        x = coords[0]
        y = coords[1]
        grid[x][y] = map_color_to_id[shape[1]]


def startingDraw(fixed_shape, shape_array):

    for row in range(ROW):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(COLUMN):
            grid[row].append(0)  # Append a cell
            if not ((row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1)):
                grid[row][column] = map_color_to_id["black"]

    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)

    # define button
    BUTTON_WIDTH = ((WIDTH+MARGIN)*COLUMN) / 2
    BUTTON_HEIGHT = 50
    button = PG.Rect(0, (HEIGHT+MARGIN) * ROW + 5, BUTTON_WIDTH, BUTTON_HEIGHT)
    # draw fixed shape
    for shape in fixed_shape:
        #print(map_color_to_id[shape.color])
        for coords in shape.domain[0]:
            x = coords[0]
            y = coords[1]
            # print("color", shape.color)
            grid[x][y] = map_color_to_id[shape.color]


    # Initialize PG
    PG.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [((WIDTH+MARGIN)*COLUMN) + 5, ((HEIGHT+MARGIN) * ROW) + BUTTON_HEIGHT]
    screen = PG.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    PG.display.set_caption("Array Backed Grid")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = PG.time.Clock()
    clock.tick(60)
    shape_drawned_count = 0
    # -------- Main Program Loop -----------
    while not done:
        for event in PG.event.get():  # User did something
            if event.type == PG.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == PG.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1 and button.collidepoint(event.pos):
                    CSPSolver(shape_array,1,grid,PG,clock,screen)
                pos = PG.mouse.get_pos()
                # cyange the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                # grid[row][column] = 1
                # print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(grey)

        # Draw the button
        PG.draw.rect(screen, red, button)
        # Draw the grid
        for row in range(ROW):
            for column in range(COLUMN):
                #color = white
                cell = grid[row][column]

                color = map_id_to_color[cell]
                #print(color)

                PG.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])

        # Go ahead and update the screen with what we've drawn.
        PG.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    PG.quit()
