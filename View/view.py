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
from DFSSolver.DFSSolver import DFSSolver
from Test.test import writeReport
from time import time
import sys



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
orange = (255,140,0)

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
    "blue": 12,
    "orange": 13
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
    12: blue,
    13: orange
}


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
COLUMN = 9
ROW = 11
N_TEST = 4
# This sets the margin between each cell
MARGIN = 5

    
# this function computes the solution and draw each steps of it. 
# The solution computing is at row 175-177, where you can see invocation of the solver (CSP or DFS)
def startingDraw(fixed_shape, shape_array, solution_choice, smart_choice, difficulty, is_test_mode):
    
    if smart_choice == 0: # if user has NOT selected "Connected Components" checks
        smart_choice = False
    else:
        smart_choice = True
    
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

    # define start_button
    START_BUTTON_WIDTH = ((WIDTH+MARGIN)*COLUMN) / 2
    START_BUTTON_HEIGHT = 50
    start_button = PG.Rect(0, (HEIGHT+MARGIN) * ROW + 5, START_BUTTON_WIDTH, START_BUTTON_HEIGHT)
    start_button_text_rect = start_button.copy()
    start_button_text_rect[0], start_button_text_rect[1] = start_button_text_rect[0] + 10, start_button_text_rect[1] + 10
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
    WINDOW_SIZE = [((WIDTH+MARGIN)*COLUMN) + 5, ((HEIGHT+MARGIN) * ROW) + START_BUTTON_HEIGHT]
    screen = PG.display.set_mode(WINDOW_SIZE)


    # Set title of screen
    text_algorithm = {1: "DFS", 2: "BT", 3: "RBT", 4: "MCBT"}
    is_with_cc = ""
    if smart_choice:
        is_with_cc = "with CC check"
    PG.display.set_caption("Level "+str(difficulty)+" with "+text_algorithm[solution_choice]+" "+is_with_cc)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = PG.time.Clock()
    clock.tick(60)
    solving_time = 0
    steps = 0

    text_is_test_mode = ""
    # -------- Main Program Loop -----------
    # Set the screen background
    screen.fill(grey)
    if is_test_mode:
            test_mode_event = PG.event.Event(0,message="testing mode")
            PG.event.post(test_mode_event)
            text_is_test_mode = "AV:"

    # MAIN LOOP TO SOLVE IQPUZZLER
    while not done:
        for event in PG.event.get():  # User did something
            if event.type == PG.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == PG.MOUSEBUTTONDOWN or (hasattr(event,'message') and event.message == 'testing mode'):
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if is_test_mode or (event.button == 1 and start_button.collidepoint(event.pos)):
                    if is_test_mode:
                        if solution_choice == 1:
                            solving_time, steps = DFSSolver(shape_array,fixed_shape,grid,PG,screen,smart_choice) 
                        else:
                            solving_time, steps = CSPSolver(shape_array,solution_choice,grid,PG,screen,smart_choice)
                          
                        writeReport(solving_time,steps,difficulty,solution_choice,smart_choice)
                        sys.exit() 
                    else:
                        if solution_choice == 1:
                            solving_time, steps = DFSSolver(shape_array,fixed_shape,grid,PG,screen,smart_choice) 
                        else:
                            solving_time, steps = CSPSolver(shape_array,solution_choice,grid,PG,screen,smart_choice)
                            # print("steo",steps)
                pos = PG.mouse.get_pos()
                # cyange the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                # grid[row][column] = 1
                # print("Click ", pos, "Grid coordinates: ", row, column)

        # Draw the start button
        # print(steps)
        PG.font.init()
        myfont = PG.font.SysFont('Comic Sans MS', 30)
        PG.draw.rect(screen, green, start_button)
        button_surface = myfont.render("SOLVE!", False, (0, 0, 0))
        screen.blit(button_surface,start_button_text_rect)
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

        # display solving time
        screen.fill(grey,(START_BUTTON_WIDTH + (MARGIN*3),(HEIGHT+MARGIN) * ROW + (MARGIN*3),300,100))
        show_time = ""
        # print("step",steps)
        if steps > 0:
            show_time = str(solving_time)[0:6]
        elif steps == -1:
            show_time = "FAIL"
        textsurface = myfont.render(text_is_test_mode + show_time, False, (0, 0, 0))
        screen.blit(textsurface,((START_BUTTON_WIDTH + (MARGIN*3),(HEIGHT+MARGIN) * ROW + (MARGIN*3))))


        # Go ahead and update the screen with what we've drawn.
        PG.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    PG.quit()
