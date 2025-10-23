#!/bin/bash

# run FreeBayes to discover variants 
freebayes -f /Users/cmdb/qb25-answers/week2/genomes/sacCer3.fa -L /Users/cmdb/qb25-answers/week3/BYxRM_bam/bamListFile.txt  --genotype-qualities -p 1 > unfiltered.vcf 

# the resulting VCF file is unfiltered, meaning that it contains low-confidence calls and also has some quirky formatting, so the following steps use a software suite called vcflib to clean up the VCF

# filter the variants based on their quality score and remove sites where any sample had missing data
vcffilter -f "QUAL > 20" -f "AN > 9" unfiltered.vcf > filtered.vcf

# FreeBayes has a quirk where it sometimes records haplotypes rather than individual variants; we want to override this behavior
vcfallelicprimitives -kg filtered.vcf > decomposed.vcf

# in very rare cases, a single site may have more than two alleles detected in your sample; while these cases may be interesting, they may also reflect technical errors and also pose a challenge for parsing the data, so we remove them
vcfbreakmulti decomposed.vcf > biallelic.vcf