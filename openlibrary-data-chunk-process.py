# With this file you can convert your txt files into smaller files which are easier to load into the db
#First, decide how you want to identify the files. I used author/editions/works so files end up looking like author_3000000, editions_3000000
#Second, decide how large you would like to make each chunk.  - in the edition table I made them 3 million lines which was about 3.24 gigs and ended up taking about an hour to load.
input = 'C:\openlibrary-search\data\ol_dump_authors_2016-07-31_processed.csv'
file_identifer = 'author'
lines_per_file = 3000000
filenames = []
csvoutputfile = None
with open(input) as cvsinputfile:
    csvreader = csv.reader(cvsinputfile, delimiter='\t') # CREATE READER
    for lineno, row in enumerate(csvreader):

        if lineno % lines_per_file == 0:
            if csvoutputfile:
                csvoutputfile.close()

            small_filename = file_identifer + '_{}.csv'.format(lineno + lines_per_file)
            filenames.append(small_filename)
            csvoutputfile = open(small_filename, "w", newline='')
            csvwriter = csv.writer(csvoutputfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if len(row) > 4:
                csvwriter.writerow([row[0], row[1], row[2], row[3], row[4]])
    if csvoutputfile:
        csvoutputfile.close()
print(file_identifer, '\n Data has now been processed.\nIMPORTANT! please copy this array and save it for use with data loader.\n', filenames)