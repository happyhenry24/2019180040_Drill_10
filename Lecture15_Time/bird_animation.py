from pico2d import *
import random

open_canvas(800, 600)

bird_image = load_image('bird_animation.png')

frame_positions = [
    (0, 0, 190, 150),
    (200, 0, 350, 150),
    (400, 0, 550, 150),
    (550, 0, 720, 150),
    (720, 0, 920, 150),
    (20, 200, 175, 340),
    (200, 200, 370, 340),
    (375, 200, 550, 340),
    (520, 200, 750, 340),
    (750, 200, 920, 340),
    (20, 390, 175, 500),
    (200, 390, 360, 500),
    (375, 390, 545, 500),
    (545, 360, 725, 490)
]

class Bird:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.frame = 0
        self.direction = 1

    def update(self):
        self.frame = (self.frame + 1) % len(frame_positions)
        self.x += self.speed * self.direction
        if self.x > 800 or self.x < 0:
            self.direction *= -1

    def draw(self):
        left, bottom, width, height = frame_positions[self.frame]
        flip = 'h' if self.direction == -1 else ''
        bird_image.clip_composite_draw(left, bottom, width, height, 0, flip, self.x, self.y, width, height)

birds = [Bird(random.randint(50, 750), random.randint(150, 450), random.uniform(2, 5)) for _ in range(10)]

while True:
    clear_canvas()

    for bird in birds:
        bird.update()
        bird.draw()

    update_canvas()
    delay(0.05)

close_canvas()
