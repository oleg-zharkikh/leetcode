self.position = (
    randint(0, GRID_WIDTH - 1) * GRID_SIZE,
    randint(0, GRID_HEIGHT - 1) * GRID_SIZE
)
while self.position in occupied_cells:
    self.position = (
    randint(0, GRID_WIDTH - 1) * GRID_SIZE,
    randint(0, GRID_HEIGHT - 1) * GRID_SIZE
)