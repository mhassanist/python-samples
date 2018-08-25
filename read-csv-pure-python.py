import os

DATA_DIR_PATH = r"C:\MSaudi\data_wrangling"
DATA_FILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []

    # f = open(datafile, "r");
    with open(datafile, "r") as f:
        count = 0;
        for line in f:
            #print line
            data.append(line)
            
            count +=1
            if count == 10:
                break

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATA_DIR_PATH, DATA_FILE)

    d = parse_file(datafile)

    print d[0]
    print d[1]
     
test()
