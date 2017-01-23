import numpy as np

class layout():
    def __init__(self,num_col, num_row,obstructed_cells, wires_list):

        # Grid size variables:
        self.num_col = num_col
        self.num_row = num_row

        # Obstruction's information:
        self.obs_cell_list = obstructed_cells

        # wiring information
        self.wires_list = wires_list
        self.num_wires = len(wires_list)

        #initialize the grid
        self.initialize_grid()

        # visualization variables:
        self.colors_dict={}
        self.build_colors()

    def initialize_grid(self):
        self.grid = np.zeros((2, self.num_col,self.num_row))

        for obs in self.obs_cell_list:
            self.grid[0,obs[0],obs[1]] = -1

        for net in range(self.num_wires):
            for pin in self.wires_list[net]:
                self.grid[0,pin[0],pin[1]] = net+1

    def build_colors(self):
        # building color code based on gnuplot2 colormap:
        self.colors_dict ={-1:0}    #obstacles are always black

        # calculating white for empty cells:
        # color length for one wire with margins:
        color_margin = (self.num_row + self.num_col)*2

        # then what is white with good margis:
        white = self.num_wires*color_margin + 6*color_margin
        self.colors_dict[0] = white

        # populating the colors list for wires to the colors dictionary:
        for wire in range(self.num_wires):
            self.colors_dict[wire+1] = (wire+3)*color_margin


    def state_2_image(self):

        image = np.zeros((self.num_row,self.num_col))

        for j in range(self.num_col):
            for i in range(self.num_row):
                if self.grid[0,j,i] == 0:
                    image[i,j] = self.colors_dict[self.grid[0,j,i]]
                else:
                    image[i,j] = self.colors_dict[self.grid[0,j,i]]

        return image



    def display(self):
        print self.grid
        import drawing as DRW

        img = self.state_2_image()
        DRW.create_Fig(img)



if __name__ == "__main__":
    lay = layout(7,5,[(0,0),(3,4)],[[(1,0),(6,4)]])
    lay.display()
