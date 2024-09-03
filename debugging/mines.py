#!/usr/bin/python3
import random
import os

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mines = set()
        self.generate_mines(mines)
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def generate_mines(self, mines):
        if mines > self.total_cells:
            raise ValueError("Number of mines exceeds grid size.")
        while len(self.mines) < mines:
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.mines.add((x, y))

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self, reveal=False):
        self.clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_victory(self):
        revealed_cells = sum(sum(row) for row in self.revealed)
        return revealed_cells == self.total_cells - len(self.mines)

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid input: Coordinates out of bounds.")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_victory():
                    self.print_board(reveal=True)
                    print("Congratulations! You've cleared all non-mine cells. You win!")
                    break
            except ValueError:
                print("Invalid input: Please enter integers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
