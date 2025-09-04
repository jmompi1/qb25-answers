#!/usr/bin/env python3

import sys
ce11_genes = open(sys.argv[1]
                  
for line in ce11_genes:
    category = line.rstrip().split("\t")
    patient = category[3]
    chrom = cstegory[0]

    original_score = int(category[4])
    strand = category [5]

    end = int(category[2])
    start = int(category[1])
    feature_length = end - start              

    new_score = original_score * feature_length 
    if strand == "-":
        new_score *= -1

    print(chrom + "\t" + str(start) + "\t" + str(end) + "\t" + patient + "\t" + str(new_score) + "\t" + patient))