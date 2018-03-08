#!/usr/bin/env python3

import csv
import sys

fr = open(sys.argv[1], 'rt')
fw = open(sys.argv[2], 'wt')

try:
	reader = csv.reader(fr)
	writer = csv.writer(fw)
	for row in reader:
		print(row)
		writer.writerow(row)

finally:
	fr.close()
	fw.close()
