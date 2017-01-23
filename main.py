import importing as LOAD

if __name__ == "__main__":
    filename = "benchmarks/stdcell.inFile"
    chip = LOAD.load_input(filename)
    chip.display()
