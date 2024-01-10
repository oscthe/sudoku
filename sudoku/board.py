import pygame
import yaml
from gui import GUI

class Board:
    def __init__(self):
        self.load_yaml()
        self.background_color = self.WHITE
        self.board_width = self.GRID_SIZE * self.CELL_SIZE
        self.board_height = self.GRID_SIZE * self.CELL_SIZE
        self.screen_width = self.board_width
        self.screen_height = self.board_height
        self.screen = pygame.display.set_mode(
            size=(self.screen_width, self.screen_height)
        )
        pygame.display.set_caption("Sudoku Game")
        self.run()

    def load_yaml(self, path: str = "config.yaml"):
        """Loads the config.yaml file and sets the attributes of the Board class to the values in the file.

        Args:
            path (str, optional): Defaults to "config.yaml".
        """
        with open(path, "r") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        for key, value in data.items():
            setattr(self, key, value)

    def run(self, running: bool = True):
        row, col = None, None
        self.initialize_board()
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                ):
                    row = event.pos[1] // self.CELL_SIZE
                    col = event.pos[0] // self.CELL_SIZE
                elif event.type == pygame.KEYDOWN and event.unicode.isdigit():
                    entered_number = int(event.unicode)
                    if 1 <= entered_number <= 9 and self.is_valid(row, col):
                        self.board[row][col] = entered_number
                        row = None
                        col = None

            self.draw_board()
            self.draw_selected_cell(row, col)
            pygame.display.flip()
            clock.tick(60)

    def initialize_board(self):
        self.board = generate_board()
        self.original_position = [
            [True if number != 0 else False for number in row] for row in self.board
        ]

    def _get_board_coordinates(self):
        # Function for creating list of lists containing x and y coordinates for each position in grid
        pass

    def draw_board(self):
        self.screen.fill(self.WHITE)
        number_font = pygame.font.Font(None, self.FONT_SIZE)
        for i in range(self.GRID_SIZE):
            thickness = 3 if i % 3 == 0 else 1
            length = round(i * self.CELL_SIZE)
            # Draw vertical line
            pygame.draw.line(
                surface=self.screen,
                color=self.BLACK,
                start_pos=(0, length),
                end_pos=(self.board_height, length),
                width=thickness,
            )
            # Draw horizontal line
            pygame.draw.line(
                surface=self.screen,
                color=self.BLACK,
                start_pos=(length, 0),
                end_pos=(length, self.board_width),
                width=thickness,
            )

        # Draw numbers
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                value = self.board[row][col]
                if value != 0:
                    font = pygame.font.Font(None, 72)
                    text = font.render(str(value), True, self.BLACK)
                    text_rect = text.get_rect(
                        center=(
                            col * self.CELL_SIZE + self.CELL_SIZE // 2,
                            row * self.CELL_SIZE + self.CELL_SIZE // 2,
                        )
                    )
                    self.screen.blit(text, text_rect)

    def draw_selected_cell(self, row, col):
        if row is not None and col is not None:
            pygame.draw.rect(
                surface=self.screen,
                color=self.BLACK,
                rect=(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE),
                width=3,
            )

    def is_valid(self, row, col):
        if not self.original_position[row][col]:
            return True
        return False

    def is_valid_click(self, position):
        pass

    def set_value(self, row, col, value):
        # Set the value at the given row and column
        pass

    def get_value(self, row, col):
        # Get the value at the given row and column
        pass


    def highlight_original_board(self):
        # Have button to highlight initial board numbers
        pass


def generate_board():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
