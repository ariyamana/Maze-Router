import layout_Class as LCS

# Initializing variables:
num_col = 0
num_row = 0
num_obstruct = 0
obstructed_cells = []
num_wires = 0
wires_list =[]

def load_input(filename):
    f = open(filename, "r")
    inFile = f.readlines()

    # Read the grid size:
    sizes = inFile[0].split()

    num_col = int(sizes[0])
    num_row = int(sizes[1])

    # Read the obstructed cells;
    num_obstruct = int(inFile[1].split()[0])

    for nline in range(2,2+num_obstruct):
        obs_temp = inFile[nline].split()
        obstructed_cells.append((int(obs_temp[0]),int(obs_temp[1])))

    # Read the wiring information
    num_wires = int(inFile[2+num_obstruct].split()[0])

    for nline in range(2 + num_obstruct + 1, 2 + num_obstruct + 1+ num_wires):
         wire_temp = inFile[nline].split()
         wire_pin_list=[]
         for npin in range(int(wire_temp[0])):
             pin = (int(wire_temp[npin*2 + 1]), int(wire_temp[npin*2 +2]))
             wire_pin_list.append(pin)
         wires_list.append(wire_pin_list)

    layout_object =LCS.layout(num_col, num_row,obstructed_cells, wires_list)
    return layout_object

if __name__ == "__main__":
    filename = "benchmarks/sydney.inFile"
    load_input(filename)
