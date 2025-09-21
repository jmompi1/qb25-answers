#!/bin/bash
#4

#Use bedtools intersect and hg19-kc.bed to determine which gene has the most SNPs
bedtools intersect -c -a hg19-kc.bed -b snps-chr1.bed | -k5,5nr > highsnps
head -1 highsnps
#ENST00000490107.6_7 is the gene that contains the highest number of SNPS in Chr 1
#The readable name is SMYD3, and located in chr1:245,912,649-246,670,581. The gene is 757,933 bp long and there are 7 exons.
#SMYD3 encodes a methyl transferase which forms a complex with  RNA polymerase II by interacting with an RNA Helicase. 
#I think this gene has the most SNPs becuase it has been detected very often as associated with different types of cancer.

bedtools sample -i snps-chr1.bed -n 20 -seed 42 > snpsubset
bedtools sort -i snpsubset > snpsubset-sorted
bedtools sort -i hg19-kc.bed > hg19-kc-sorted.bed
bedtools closest -d -t first -a snpsubset-sorted.bed -b hg19-kc-sorted.bed > comb-sorted.bed
awk '$11 == 0' comb-sorted.bed | wc -l
#there are 15 SNPs in a gene
#there is a range of 21280 between SNPS outside the gene