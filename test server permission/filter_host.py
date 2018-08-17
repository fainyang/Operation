import csv
import re

filename='failed_host.csv'

rf = open(filename,'r') 
reader = csv.reader(rf)
L=[]
for row in reader:
	if 'UNREACHABLE' in  row[0]:
		p = re.findall( r'[0-9]+(?:\.[0-9]+){3}', row[0] )
		L.append(p[0])
L.sort()

for row in L:
	print(row)