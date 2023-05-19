from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 605
TOP = 239
RIGHT = 1293
BOTTOM = 927

EMPTY = 0
Red = 1
Black = 2
KING_RED = 3
KING_Black = 4


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(8)] for j in range(8)]

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == Red:
                    print("R", end=" \t")
                elif grid[i][j] == Black:
                    print("B", end=" \t")
                elif grid[i][j] == KING_Black:
                    print("KB", end=" \t")
                elif grid[i][j] == KING_RED:
                    print("KR", end=" \t")
            print("\n")
        print("#####################################\n")



    def _convert_grid_to_color(self, grid):
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                print(i, j)
                print('\n')
                print(grid[i][j])
                print('\n')
                if (grid[i][j] == (152,1,0) or grid[i][j] == (153,0,0)):
                    grid[i][j] = KING_RED
                elif grid[i][j] == (51,51,51):
                    grid[i][j] = KING_Black   
                elif grid[i][j][0] < 100:
                    grid[i][j] = Black # BLAAACK
                elif grid[i][j][1] <= 50:
                    grid[i][j] = Red
                else:
                    grid[i][j] = EMPTY;
        return grid

    def _get_grid_cordinates(self):
        startCord = (49, 47)
        cordArr = []
        for i in range(0, 8):
            for j in range(0, 8):
                x = startCord[0] + i * 85.5
                y = startCord[1] + j * 85.5
                print(i,j)
                print('\n')
                print(x,y)
                print('\n')
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(8)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 8 == 0 and index != 0: 
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        #cropedImage.show()

        pixels = self._convert_image_to_grid(cropedImage)
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)


        self.board = new_grid

        return (self.board, is_game_end)

    def select_column(self, x,y):
        pyautogui.click(
            LEFT + 48 + y * 82,
            TOP + 42 + x * 82,
        )