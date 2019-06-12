import re
with open("/home/arun/Documents/Shohaney.factera.fusions.txt", 'r') as myfile:
     with open("/home/arun/Documents/Shohaney.factera.fusions.csv", 'w') as csv_file:
             for line in myfile:
                     fileContent = re.sub("\t", ",", line)
                     csv_file.write(fileContent)

