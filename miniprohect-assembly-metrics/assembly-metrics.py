#!/usr/bin/env/ python3

import sys
import fasta



my_file = open( sys.argv[1] )
contigs = fasta.FASTAReader(my_file)

i = 0
length = 0

for ident, sequence in contigs:
    length = int(length + len(sequence))
    i = int(i + 1)
avg_length = length/i
my_file.close()

my_file = open( sys.argv[1] )
contigs = fasta.FASTAREADER(my_file)
contig_lengths = []


for ident, sequence in contigs:
    len_contig = int(len(sequence))
    contig_lengths.append(len_contig)
contig_lengths.sort(reverse = True)

len_cum = 0
cumulative_length = []
for length in contig_lengths:
    cumulative_length.append(length)
    len_cum = len_cum + length
    if len_cum > (length*0.5):
        print(f"The length of the shortest contig at 50% of the total assembly length is {length}")

