import time
import random
import msvcrt
import os

os.system("")

class Bubble:
    def __init__(self, x, y, speed, symbol, phase, amplitude):
        self.x = x
        self.y = y
        self.base_x = x
        self.speed = speed
        self.symbol = symbol
        self.phase = phase
        self.amplitude = amplitude
        self.direction = 1

    def update(self, width, height):
        # движение пузырька верх
        self.y -= self.speed

        if self.y < 0:
            self.y = height - 1
            self.base_x = random.randint(1, width - 2)
            self.x = self.base_x
            self.phase = 0

        # горизонтальное покачивание
        self.phase += 0.2 * self.direction

        # изменения направления покачивания
        if self.phase >= self.amplitude:
            self.phase = self.amplitude
            self.direction = -1

        elif self.phase <= -self.amplitude:
            self.phase = -self.amplitude
            self.direction = 1

        # обновление горизонтальной координаты
        self.x = self.base_x + self.phase

        if self.x < 1:
            self.x = 1

        elif self.x > width - 2:
            self.x = width - 2

def draw_screen(bubbles, width, height):
    # пустое игровое поле
    screen = []

    for row in range(height):
        screen.append([" "] * width)

    # размещение пузырьков на игровом поле
    for bubble in bubbles:
        x = round(bubble.x)
        y = round(bubble.y)

        if 0 <= x < width and 0 <= y < height:
            screen[y][x] = bubble.symbol

    # формирует верхнюю границу
    frame = "+" + "-" * width + "\n"

    # добавляет содержимое игрового поля
    for row in screen:
        frame += "|" + "".join(row) + "|\n"

    # формирует нижнюю границу
    frame += "+" + "-" * width + "+"

    # вывод изображения в терминал
    print("\033[H" + frame, end="", flush = True)

def run_animation():
    width = 30
    height = 10

    running = True
    paused = False
    bubbles = [
        Bubble(5, 9, 0.5, "o", 0, 2),
        Bubble(15, 8, 1.0, "O", 0, 3)
    ]

    print("\033[2J\033[H", end="")

    while running:
        if msvcrt.kbhit():
            key = msvcrt.getch().lower()

            if key == b'q':
                running = False

            elif key == b' ':
                paused = not paused

            elif key == b'+' or key == b'=':
                for bubble in bubbles:
                    bubble.speed += 0.2


                    if bubble.speed > 2.0:
                        bubble.speed = 2.0

            elif key == b'-':
                for bubble in bubbles:
                    bubble.speed -= 0.2

                    if bubble.speed < 0.2:
                        bubble.speed = 0.2

            elif key == b'b':
                new_x = random.randint(1, width - 2)
                new_speed = random.uniform(0.3, 1.0)
                new_symbol = random.choice(["o", "O"])

                bubbles.append(
                    Bubble(new_x, height - 1, new_speed, new_symbol, 0, 2)
                )

        if paused:
            time.sleep(0.1)
            continue

        for bubble in bubbles:
            bubble.update(width, height)

        draw_screen(bubbles, width, height)

        time.sleep(0.1)

if __name__ == "__main__":
    run_animation()