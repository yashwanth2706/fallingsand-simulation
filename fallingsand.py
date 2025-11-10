import pygame, sys

# Initialize pygame
pygame.init()

# Setup height, width, FPS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 120 # 120 for fulidity
GREY = (29, 29, 29)

# Setup game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Add name (caption) to window
pygame.display.set_caption("Falling Sand")

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
    window.fill(GREY)
    
    pygame.display.flip()
    clock.tick(FPS)