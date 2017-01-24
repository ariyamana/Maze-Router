import numpy as np
import drawing as DRW

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
        self.routing_current_wire = 0

        #initialize the grid
        self.initialize_grid()

        # visualization variables:
        self.colors_dict={}
        self.build_colors()
        self.image_counter = 0


    def initialize_grid(self):
        self.grid = np.zeros((2, self.num_col,self.num_row))

        for obs in self.obs_cell_list:
            self.grid[0,obs[0],obs[1]] = -1

        for net in range(self.num_wires):
            for pin in self.wires_list[net]:
                self.grid[0,pin[0],pin[1]] = net+1

        for i in range(self.num_row):
            for j in range(self.num_col):
                self.grid[1,j,i] = 2*(self.num_row*self.num_col)


    def reset_propagation(self):
        for i in range(self.num_row):
            for j in range(self.num_col):
                self.grid[1,j,i] = 2*(self.num_row*self.num_col)

    def get_closest(self,cell):
        closest = (2*(self.num_row*self.num_col),2*(self.num_row*self.num_col))
        current_dist = 2*(self.num_row*self.num_col)

        self.get_neighbour(cell)


        for key in self.cell_available_nghbrs.keys():
            nghbr = self.cell_available_nghbrs[key]

            if  nghbr != -1 :
                if self.grid[1,nghbr[0], nghbr[1]] < current_dist:
                    current_dist = self.grid[1,nghbr[0], nghbr[1]]
                    closest = (nghbr[0],nghbr[1])
        return closest

    def get_neighbour(self, cell):
        #initializing an empty dictionary for storing available neighbours:
        self.cell_available_nghbrs ={'left':-1,'right':-1,'up':-1, 'down':-1}

        # Left:
        if cell[0] > 0:
            if self.grid[0,cell[0]-1,cell[1]] == 0:
                self.cell_available_nghbrs['left'] = (cell[0]-1, cell[1])

        # Up:
        if cell[1] > 0:
            if self.grid[0,cell[0],cell[1]-1] == 0:
                self.cell_available_nghbrs['up'] = (cell[0],cell[1]-1)

        # Right:
        if cell[0] < self.num_col-1:
            if self.grid[0,cell[0]+1,cell[1]] == 0:
                self.cell_available_nghbrs['right'] = (cell[0]+1, cell[1])

        # Down:
        if cell[1] < self.num_row-1:
            if self.grid[0,cell[0],cell[1]+1] == 0:
                self.cell_available_nghbrs['down'] = (cell[0], cell[1]+1)



    def metropolis_distance(self,p1,p2):
        distance = np.abs(p1[0]-p2[0]) + np.abs(p1[1]-p2[1])
        return distance

    def route_single(self,wire, source,sink):
        queue = [source]
        self.display()
        self.routing_current_wire = wire
        self.grid[1,source[0],source[1]] = 0

        while len(queue) > 0:
            #Pick the first item in the queue:
            (j,i) = queue[0]

            # find the metropolis distance of the point to the source
            r1 = self.metropolis_distance((j,i),source)

            # set the distance value in the current place:
            self.grid[1,j,i] = r1

            #remove this item from the queue:
            queue.pop(0)

            # display
            # self.display()

            # check if we arrived:
            r2 = self.metropolis_distance((j,i),sink)
            if r2==1:
                print "propagation successfull."
                break
            else:
                # add the neighbours of this point to the queue:
                self.get_neighbour((j,i))
                for key in self.cell_available_nghbrs.keys():
                    if self.cell_available_nghbrs[key] != -1 :
                        queue.append(self.cell_available_nghbrs[key])

        # display
        self.display()

        # Back propagation

        current_cell = (sink[0],sink[1])

        while True:
            closest_cell = self.get_closest(current_cell)

            # add this cell to the wire
            self.grid[0,closest_cell[0],closest_cell[1]] = self.routing_current_wire

            # replace the closest with the current cell:
            current_cell = (closest_cell[0],closest_cell[1])

            # check if we arrived:
            r3 = self.metropolis_distance(current_cell,source)

            if r3 ==1:
                print "Backtracking  successfull."
                break

            # display
            # self.display()

        self.reset_propagation()

        # display
        self.display()





    def build_colors(self):
        # building color code based on gnuplot2 colormap:
        self.colors_dict ={-1:0}    #obstacles are always black

        # calculating white for empty cells:
        # color length for one wire with margins:
        color_margin = (self.num_row + self.num_col)*6

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
                    if self.routing_current_wire > 0:
                        if  self.grid[1,j,i] < 2*self.num_row*self.num_col:
                            image[i,j] = self.colors_dict[self.routing_current_wire] + 6*self.grid[1,j,i]
                else:
                    image[i,j] = self.colors_dict[self.grid[0,j,i]]

        return image



    def display(self):

        #print self.grid


        current_image = self.state_2_image()

        if self.image_counter  == 0:
            self.figure_object, self.image_object = DRW.create_Fig(current_image)
        else:
            DRW.draw_State(self.figure_object, self.image_object, current_image, .001)

        self.image_counter = self.image_counter + 1



if __name__ == "__main__":
    lay = layout(7,5,[(0,0),(3,4)],[[(1,0),(6,4)]])
    #lay.display()
    lay.route_single(1, (1,0), (6,4))
    #lay.display()
