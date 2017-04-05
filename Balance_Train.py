import random
import sys
import csv
# clean duplicated comments
entries = set()

print "Removing duplicated from "+sys.argv[1]+'.tsv'
with open(sys.argv[1]+"_balanced.tsv", mode='w') as fd_writer:
    with open(sys.argv[1]+".tsv", mode='r') as fd_reader:
        reader = csv.reader(fd_reader, delimiter='\t', lineterminator='\n')

        writer = csv.writer(fd_writer, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            key = (row[1], row[2]) # key is star+comment
           
            if key not in entries:
              writer.writerow(row)
              entries.add(key)
    
fd_writer.close
fd_reader.close
complete_dict = {}
filling_dict = {}

with open(sys.argv[1]+"_balanced.tsv", mode='r') as fd_reader:
    reader = csv.reader(fd_reader, delimiter='\t', lineterminator='\n')
    skip_header=0
    for row in reader:
        
        if skip_header==1:
            
            if str(row[1]) not in complete_dict:
                complete_dict[str(row[1])]=1
            else:
                complete_dict[str(row[1])]+=1
        else:
            skip_header=1
fd_reader.close

print complete_dict
max_items = min(complete_dict.values())
print "Maximum number of samples: ", max_items

with open(sys.argv[1]+"_balanced_min.tsv", mode='w') as fd_writer:
    writer = csv.writer(fd_writer, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    with open(sys.argv[1]+"_balanced.tsv", mode='r') as fd_reader:
        reader = csv.reader(fd_reader, delimiter='\t', lineterminator='\n')
        for row in reader:
            if str(row[1]) not in filling_dict:
                filling_dict[str(row[1])]=1
                writer.writerow(row)
            else:
                filling_dict[str(row[1])]+=1
                if filling_dict[str(row[1])]<=max_items:
                    writer.writerow(row)