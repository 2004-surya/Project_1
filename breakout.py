import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 20
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 100, 40
BRICK_GAP = 5
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BRICK_COLORS = [RED, BLUE]

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Clone")

# Paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = 5, 5

# Bricks
bricks = []
for row in range(3):
    for col in range(8):
        brick = pygame.Rect(col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP, row * (BRICK_HEIGHT + BRICK_GAP) + BRICK_GAP,
                            BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 5

    # Check game over
    if ball.top >= HEIGHT:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, paddle)
    pygame.draw.rect(window, BLUE, ball)
    for idx, brick in enumerate(bricks):
        pygame.draw.rect(window, BRICK_COLORS[idx % len(BRICK_COLORS)], brick)
    pygame.display.update()
    pygame.time.delay(30)



