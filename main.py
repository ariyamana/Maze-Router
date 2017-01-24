import importing as LOAD
import sys
def main(filename):
        # filename = ["benchmarks/sydney.inFile",
        #   "benchmarks/stanley.inFile",
        #   "benchmarks/impossible.inFile",
        #   "benchmarks/oswald.inFile",
        #   "benchmarks/rusty.inFile",
        #   "benchmarks/misty.inFile",
        #   "benchmarks/wavy.inFile",
        #   "benchmarks/kuma.inFile",
        #   "benchmarks/impossible2.inFile",
        #   "benchmarks/temp.inFile",
        # "benchmarks/stdcell.inFile"]

        chip = LOAD.load_input(filename)
        chip.display()
        chip.routing()
        chip.display()

if __name__ == "__main__":


    main(sys.argv[1])
