import pygame
import random
import string
import time

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Letter Typing Game")

# Define fonts and colors
font = pygame.font.Font(None, 100)
score_font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 40)

# Colors
bg_color = (30, 30, 30)
letter_color = (255, 255, 255)
correct_color = (0, 255, 0)
wrong_color = (255, 0, 0)
score_color = (0, 255, 0)
button_color = (70, 130, 180)
button_hover_color = (100, 149, 237)

# Game variables
score = 0
letter = random.choice(string.ascii_lowercase)
start_time = time.time()
game_over = False

# Function to display text
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to create a button
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            restart_game()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    display_text(text, button_font, (255, 255, 255), x + width / 2, y + height / 2)

# Restart the game
def restart_game():
    global score, letter, start_time, game_over
    score = 0
    letter = random.choice(string.ascii_lowercase)
    start_time = time.time()
    game_over = False

# Game loop
def letter_game():
    global score, letter, start_time, game_over
    running = True
    while running:
        screen.fill(bg_color)

        if game_over:
            # Display the score and the restart button
            display_text(f"Final Score: {score}", score_font, score_color, screen_width // 2, screen_height // 2 - 50)
            button("Restart", screen_width // 2 - 100, screen_height // 2 + 50, 200, 50, button_color, button_hover_color, restart_game)
        else:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif pygame.key.name(event.key) == letter:
                        score += 1
                        letter = random.choice(string.ascii_lowercase)
                        start_time = time.time()  # reset time after correct letter
                        letter_color = correct_color  # Set to green when correct
                    else:
                        letter_color = wrong_color  # Set to red when wrong
                        running = False

            # Display the letter and score
            display_text(letter, font,(255, 255, 255), screen_width // 2, screen_height // 2)
            display_text(f"Score: {score}", score_font, score_color, screen_width // 2, screen_height - 50)

            # Check if time to display the current letter has run out (5 seconds limit)
            if time.time() - start_time > 5:
                display_text("Time's up!", score_font, wrong_color, screen_width // 2, screen_height // 2)
                pygame.display.flip()
                time.sleep(1)  # Show the "time's up" message for 1 second
                game_over = True

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        pygame.time.Clock().tick(30)

# Run the game
letter_game()
# Quit pygame
pygame.quit()
