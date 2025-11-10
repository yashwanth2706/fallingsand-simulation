import pygame, sys
from grid import Grid

# Initialize pygame
pygame.init()

# Setup height, width, FPS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20 # Total Cells = (800/20) * (600/20) = 1200
FPS = 120 # 120 for fulidity
GREY = (29, 29, 29)

# Setup game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Add name (caption) to window
pygame.display.set_caption("Falling Sand")

# clock object to control the framerate of the simulation
clock = pygame.time.Clock()
grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    
    # 1. Event Handling
    # pygame.event.get() returns the list of all the events recognized by pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 2. Update State
    
    # 3. Drawing
    window.fill(GREY)
    grid.draw(window)
    
    pygame.display.flip()
    clock.tick(FPS)