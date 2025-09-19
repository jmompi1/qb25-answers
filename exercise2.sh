#!/bin/bash
#2
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg16/bigZips/hg16.chrom.sizes
grep -v _ hg16.chrom.sizes > hg16-main.chrom.sizes
bedtools makewindows -g  hg16-main.chrom.sizes -w  1000000 > hg16-1mb.bed
cut -f1-3,5 hg16-kc.tsv > hg16kc.bed
bedtools intersect -c -a hg16-1mb.bed -b hg16-kc.bed > hg16-kc-count.bed



wc hg19-kc.bed
#there are 80,270 genes in hg19
bedtools intersect -v -a hg19-kc.bed -b hg16-kc.bed > hg19-unique.bed
wc hg19-unique.bed
#There are 42717 genes that are unique to hg19
#Since hg19 is un updated version of the human genome, they probably have higher resolution and were able to identify new genes. Maybe the sequences were the same but they were not structurally defined as genes in the hg16.

wc hg16-kc.bed
#There are 21365 genes in hg16

wc hg16-unique.bed
#There are 3460 genes unique to hg16
#Some regions labeled as genes in hg16 may have been updated in the hg19 as intergenic regions, or "merged" with another seuence under a new gene name in hg19.


