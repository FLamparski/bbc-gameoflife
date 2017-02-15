from copy import deepcopy

# Helper for getting the state of a given cell,
# can return a value if the cell is out of bounds.
def get_cell(state, x, y, else_val=0):
	try:
		return state[y][x]
	except IndexError as e:
		return else_val

# Helper for determining if the cell is alive
def is_alive(state, x, y):
	return get_cell(state, x, y) == 1

# Could this be converted to a simple function?
# This class does not store any state.
# Nonetheless, I left it like this as external
# tests may expect a class to be here.
class Life(object):
	def evolve(self, state):
		# Assume a square board for simplicity.
		# Assume that the size of the board is fixed,
		# and no new board space needs to be created if
		# live cells move out of bounds.
		size = len(state)

		# Create a copy of the board. The new state
		# is computed from the old state only.
		new_state = deepcopy(state)

		# Iterate through all the cells in the old state
		# and apply rules.
		for y in range(len(state)):
			for x in range(len(state[y])):
				# Since live cells are represented by 1s and dead cells by 0s,
				# we can count live neighbours by summing over the list of
				# all neighbours.
				n_neighbours = sum([
					# horizontal neighbours
					get_cell(state, x - 1, y),
					get_cell(state, x + 1, y),
					# vertical neighbours
					get_cell(state, x, y - 1),
					get_cell(state, x, y + 1),
					# diagonal neighbours
					get_cell(state, x - 1, y - 1),
					get_cell(state, x - 1, y + 1),
					get_cell(state, x + 1, y + 1),
					get_cell(state, x + 1, y - 1)
				])

				# Fewer than 2 adjacent cells, the cell should die.
				if is_alive(state, x, y) and n_neighbours < 2:
					new_state[y][x] = 0

				# More than 3 adjacent cells, the cell should die.
				if is_alive(state, x, y) and n_neighbours > 3:
					new_state[y][x] = 0

				# Dead and exactly 3 adjacent living cells,
				# the cell should become alive.
				if not is_alive(state, x, y) and n_neighbours == 3:
					new_state[y][x] = 1

		return new_state
