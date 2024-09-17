import pygame as pg
from math import sin, cos
from bird import Bird

class Background(pg.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = load_image("background.jpg")
        self.rect = self.image.get_rect()
        self.scroll_speed = 2

    def update(self):
        # Scroll the background to the left
        self.rect.x += self.scroll_speed
        if self.rect.right <= 0:
            self.rect.x = self.screen.get_width()

class PipeGroup(pg.sprite.Group):
    def add_pipe(self, pipe):
        super().add(pipe)
        pipe.rect.x = self.screen_width + pipe.rect.width

    @property
    def screen_width(self):
        return self.screen.get_width()


def update_score(pipes, bird):
    # Increment the score if the bird passes the pipes
    for pipe in pipes:
        if not pipe.passed and pipe.rect.right <= bird.rect.x + bird.rect.width:
            pipe.passed = True
            return bird.score + 1
    return bird.score

def check_collision(bird, pipes):
    # Check for collisions between the bird and all pipes
    for pipe in pipes:
        if collide_rect(bird.rect, pipe.upper_pipe) or collide_rect(bird.rect, pipe.lower_pipe):
            return True
    return False

def display_score(screen, score):
    # Display the current score on the top-right corner of the screen
    font = pg.font.Font(None, 48)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (730, 10))

def main():
    # Initialize Pygame and display settings
    pg.init()
    screen = pg.display.set_mode((800, 500))

    bg = Background(screen)
    pipes = PipeGroup()
    bird = Bird(100, 200)

    clock = pg.time.Clock()
    score = 0
    game_over = False

    while not game_over:
        # Event handling and input processing
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            elif event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                bird.jump()

        # Update game objects based on the new state
        bg.update()
        pipes.update(bird.rect.y)
        bird.update(bg.height)
        score = update_score(pipes, bird)

        # Check for collisions and game over conditions
        if check_collision(bird, pipes):
            game_over = True

        # Render all the elements on the screen
        screen.fill((255, 255, 255))
        bg.draw(screen)
        pipes.draw(screen)
        bird.draw(screen)
        display_score(screen, score)

        # Refresh the display
        pg.display.flip()

        # Set the frame rate and limit FPS
        frames_per_second = 60
        clock.tick(frames_per_second)

def load_image(filename):
    try:
        fullpath = f"C:/Users/LauraKhadas/Prompt_Engineering/flappy_bird/Images/{filename}"
        print(f"Loading image from: {fullpath}")  # Debugging line
        with open(fullpath, "rb") as imgfile:
            imgdata = pg.image.load(imgfile)
            return imgdata
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None




if __name__ == "__main__":
    main()





