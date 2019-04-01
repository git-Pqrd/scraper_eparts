import glob, os, csv
 
count= 0
row_to_write = []

for x, file in enumerate(glob.glob("./precision_roller/toner_cartridge*.csv")):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            count += 1
            row_to_write.append([count] + row)


with open('./cs_combined_toner.csv', mode='w') as combine:
    combine_writer = csv.writer(combine, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in row_to_write: 
        combine_writer.writerow(row)


