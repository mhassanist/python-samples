import os

DATA_DIR_PATH = r"C:\MSaudi\data_wrangling"
DATA_FILE = "beatles-diskography.csv"


#Read csv file with each line as dictionary in python 
def parse_file(datafile):
    
    with open(datafile, mode='r') as infile:
        data = []
        row_dict  = {}

        firstline=infile.readline()
        firstline_splited = firstline.split(',')

        #print firstline_splited[0].strip()

        for line in infile:
            row_splited = line.split(',')
            count = 0
            for str_part in row_splited:
                row_dict[str(firstline_splited[count].strip())] = str(str_part.strip())
                count +=1
            #print row_dict
            data.append(row_dict)
            row_dict = {}   
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATA_DIR_PATH, DATA_FILE)

    d = parse_file(datafile)
    #print d[0]
    
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

   
    assert d[0] == firstline
    assert d[9] == tenthline
     
test()
