# With this file you can convert your txt files into smaller files which are easier to load into the db
#First, decide how you want to identify the files. I used author/editions/works so files end up looking like author_3000000, editions_3000000
#Second, decide how large you would like to make each chunk.  - in the edition table I made them 3 million lines which was about 3.24 gigs and ended up taking about an hour to load.
import csv
import sys
import os
from os import listdir
from os.path import isfile, join
csv.field_size_limit(sys.maxsize)

input_path = "./data/unprocessed/"
output_path = "./data/processed/"

file_identifers = ['authors', 'works', 'editions']
filenames_array = []
lines_per_file = 2000000
for file_identifer in file_identifers:
    print('Currently processing:...', file_identifer)
    filenames = []
    csvoutputfile = None
  
    with open(os.path.join(input_path, ('ol_dump_' + file_identifer + '.txt')))as cvsinputfile:
        csvreader = csv.reader(cvsinputfile, delimiter='\t') # CREATE READER
        for lineno, row in enumerate(csvreader):

            if lineno % lines_per_file == 0:
                if csvoutputfile:
                    csvoutputfile.close()

                small_filename = file_identifer + '_{}.csv'.format(lineno + lines_per_file)
                filenames.append(small_filename)
                csvoutputfile = open(os.path.join(output_path, small_filename), "w", newline='')
                csvwriter = csv.writer(csvoutputfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if len(row) > 4:
                    csvwriter.writerow([row[0], row[1], row[2], row[3], row[4]])
        if csvoutputfile:
            csvoutputfile.close()
    filenames_array.append(filenames)
    print('\n', file_identifer, 'text file has now been processed.\n')

# write a list of filename so that its easy to copy later.
filenamesoutput = open(os.path.join(output_path, 'filenames.txt'), "w", newline='')
for row in filenames_array:
        filenamesoutput.write(','.join(["'%s'" % a for a in row]) + '\n')
filenamesoutput.close()
print('Process now completed. Please check out data/processed/filenames.txt for a list of file names.')
