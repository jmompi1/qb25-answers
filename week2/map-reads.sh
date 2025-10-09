#!/bin/bash

for sample in A01_01 A01_02 A01_03 A01_04 A01_05 A01_06
do 
    ls -l ~/Data/BYxRM/fastq/$sample.fq.gz
    echo "***" $sample                    #to use variable, prefix it with $
    bowtie2 -p 4 -x ../genomes/sacCer3 -U ~/Data/BYxRM/fastq/$sample.fq.gz > $sample.sam 
    #bowtie2 $sample.fq.gz 
    samtools sort -o $sample.bam $sample.sam
    samtools index $sample.bam
    samtools idxstats $sample.bam > $sample.idxstats
done 



