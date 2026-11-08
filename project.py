print("hello world")
# can you see this?

# confetti (in our case money)
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Pygame Confetti Effect")
clock = pygame.time.Clock()

# Confetti Particle Class (Acts like an independent "Turtle")
class ConfettiParticle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, 0)  # Start just above the screen
        self.size_width = random.randint(8, 12)
        self.size_height = random.randint(4, 8)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Movement speeds (like turtle speed/heading)
        self.speed_y = random.uniform(2, 5)   # Falling speed
        self.speed_x = random.uniform(-1, 1)  # Drifting side-to-side
        self.rotation_speed = random.uniform(5, 15)
        self.angle = random.randint(0, 360)

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        self.angle += self.rotation_speed

        # Reset particle to the top if it falls off the screen
        if self.y > HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, WIDTH)

    def draw(self, surface):
        # Create a tiny surface for the confetti piece to allow rotation
        confetti_surf = pygame.Surface((self.size_width, self.size_height), pygame.SRCALPHA)
        pygame.draw.rect(confetti_surf, self.color, (0, 0, self.size_width, self.size_height))
        
        # Rotate the piece (simulating a turning turtle)
        rotated_surf = pygame.transform.rotate(confetti_surf, self.angle)
        new_rect = rotated_surf.get_rect(center=(self.x, self.y))
        
        surface.blit(rotated_surf, new_rect.topleft)

# Create a list of 100 confetti pieces
confetti_list = [ConfettiParticle() for _ in range(150)]

# Main Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.type == pygame.QUIT:
            running = False

    # Clear screen with a dark background
    screen.fill((30, 30, 30))

    # Update and draw all confetti particles
    for confetti in confetti_list:
        confetti.move()
        confetti.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()



