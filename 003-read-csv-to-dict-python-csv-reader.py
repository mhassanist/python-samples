import csv
import os

DATA_DIR_PATH = r"C:\MSaudi\data_wrangling"
DATA_FILE = "beatles-diskography.csv"

datafile = os.path.join(DATA_DIR_PATH, DATA_FILE)

data = {}

with open(datafile) as csv_file:
    #reader() Return a reader object which will iterate over lines in the given

    csv_reader = csv.reader(csv_file, delimiter=',')
    #for line in csv_reader:
    #    print line
   
    csv_dreader = csv.DictReader(csv_file, delimiter=',')
    for line in csv_dreader:
        print line
