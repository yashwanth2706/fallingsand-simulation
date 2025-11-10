import pygame, sys

# Initialize pygame
pygame.init()

# Setup height and width
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Setup game window
window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
# Add name (caption) to window
pygame.display.set_caption("Failling Sand")

# clock object to control the framerate of the simulation
clock = pygame.time.Clock()

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