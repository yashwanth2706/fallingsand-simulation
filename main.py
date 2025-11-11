import pygame, sys
from simulation import Simulation

# Initialize pygame
pygame.init()

# Setup height, width, FPS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 6 # Total Cells = (800/20) * (600/20) = 1200
FPS = 120 # 120 for fulidity
GREY = (29, 29, 29)

# Setup game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Add name (caption) to window
pygame.display.set_caption("Falling Sand")

# clock object to control the framerate of the simulation
clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    
    # 1. Event Handling
    simulation.handel_controls()
        
    # 2. Update State
    simulation.update()
    
    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)
    
    pygame.display.flip()
    clock.tick(FPS)