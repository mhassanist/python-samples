import os #for file path functionality only.

DATA_DIR_PATH = r"C:\MSaudi\data_wrangling"
DATA_FILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    #f = open(datafile, "r");
    # open fcuntion : opens a file returning an iterator object of the file type
    # common functions in the file object are: read, readline,seek, writeline, write and close
    # The file object handle is an iterator. After iterating over the file, 
    #the pointer will be positioned at EOF (end of file) and the iterator will raise StopIteration which exits the loop
    # A file object is its own iterator, for example iter(f) returns f (unless f is closed). When a file is used as an iterator, 
    #typically in a for loop (for example, for line in f: print line), the next() method is called repeatedly.
    
    #open the file and read line by line and ads every read line to the list named data   
    with open(datafile, "r") as f:
        for line in f:
            #print line
            data.append(line)
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATA_DIR_PATH, DATA_FILE)

    d = parse_file(datafile)

    print d[0]
    print d[1]
     
test()
