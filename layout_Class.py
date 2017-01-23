import numpy as np
class layout():
    def __init__(self,num_col, num_row,obstructed_cells, wires_list):

        # Grid size variables:
        self.grid_num_col = num_col
        self.grid_num_row = num_row

        # Obstruction's information:
        self.obs_cell_list = obstructed_cells

        # wiring information
        self.wires_list = wires_list
        self.num_wires = len(wires_list)

        #initialize the grid
        self.initialize_grid()

    def initialize_grid(self):
        self.grid = np.zeros((2, self.grid_num_col,self.grid_num_row))

        for obs in self.obs_cell_list:
            self.grid[0,obs[0],obs[1]] = -1

        for net in range(self.num_wires):
            for pin in self.wires_list[net]:
                self.grid[0,pin[0],pin[1]] = net+1

    def display(self):
        print self.grid

if __name__ == "__main__":
    lay = layout(7,5,[(0,0),(3,4)],[[(1,0),(6,4)]])
    lay.display()
