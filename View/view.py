"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

grid = []

# Define some colors
black = (0, 0, 0)
lightgreen = (202,255,112)
brown = (184,134,11)
white = (255, 255, 255)
purple = (147,112,219)
green = (0,128,0)
yellow = (238,238,0)
pink = (255,182,193)
violet = (199,21,133)
red = (205,0,0)
grey = (193,205,205)

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
    "chan": 10,
    "red": 11
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
    10: red,
    11: grey
}


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 65
HEIGHT = 65
COLUMN = 9
ROW = 11

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
# draw as black box some cells such that final grid contains only diagonal cells
    

def drawSingleShape(shape):
    for coords in shape[1]:
        x = coords[0]
        y = coords[1] 
        grid[y][x] = map_color_to_id[shape[0]]


def startDraw(fixed_shape): 

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
    
    # draw fixed shape
    for shape in fixed_shape:
        #print(map_color_to_id[shape[0]])
        for coords in shape[1]:
            x = coords[0]
            y = coords[1]
            grid[y][x] = map_color_to_id[shape[0]]
        
    
    # Initialize pygame
    pygame.init()
    
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [650, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                # grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
    
        # Set the screen background
        screen.fill(grey)
    
        # Draw the grid
        for row in range(ROW):
            for column in range(COLUMN):
                #color = white
                cell = grid[row][column]
                
                color = map_id_to_color[cell]
                #print(color)
                
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
    
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
