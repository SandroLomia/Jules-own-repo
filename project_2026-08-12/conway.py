class Grid:
    def __init__(self, width, height, cells=None):
        self.width = width
        self.height = height
        if cells is None:
            self.cells = [[0 for _ in range(width)] for _ in range(height)]
        else:
            self.cells = cells

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        return 0

    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                count += self.get_cell(x + dx, y + dy)
        return count

    def next_generation(self):
        new_cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.cells[y][x] == 1:
                    if neighbors in (2, 3):
                        new_cells[y][x] = 1
                    else:
                        new_cells[y][x] = 0
                else:
                    if neighbors == 3:
                        new_cells[y][x] = 1
        self.cells = new_cells

    def __str__(self):
        res = ""
        for row in self.cells:
            for cell in row:
                res += "■" if cell else "□"
            res += "\n"
        return res
